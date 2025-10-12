import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { homedir } from "node:os";
import { parse, modify, applyEdits } from "jsonc-parser";
import path from "node:path";

const args = process.argv.slice(2);
const secretPath = args[0]; // 引数で指定された場合

const settingsPath = path.join(
  homedir(),
  ".vscode-server/data/Machine/settings.json"
);

// === 1. トークン取得 ===
let token = null;

if (secretPath) {
  if (!existsSync(secretPath)) {
    console.error(`❌ Secret file not found: ${secretPath}`);
    process.exit(1);
  }
  token = readFileSync(secretPath, "utf8").trim();
  console.log(`🔑 Token loaded from file: ${secretPath}`);
} else if (process.env.AWS_BEARER_TOKEN_BEDROCK) {
  token = process.env.AWS_BEARER_TOKEN_BEDROCK.trim();
  console.log(`🔑 Token loaded from environment variable AWS_BEARER_TOKEN_BEDROCK`);
} else {
  console.error("❌ No token source provided (neither file path nor AWS_BEARER_TOKEN_BEDROCK env var).");
  process.exit(1);
}

// === 2. AWS_REGION を取得 ===
const region = process.env.AWS_REGION?.trim() || "ap-northeast-1";
console.log(`🌏 Using AWS_REGION=${region}`);

// === 3. settings.json 読み込み ===
let text = "{}";
if (existsSync(settingsPath)) {
  text = readFileSync(settingsPath, "utf8");
}

const json = parse(text, [], { allowTrailingComma: true, disallowComments: false }) ?? {};

// === 4. claude-code.environmentVariables の更新内容 ===
const envVars = [
  { name: "CLAUDE_CODE_USE_BEDROCK", value: "1" },
  { name: "AWS_BEARER_TOKEN_BEDROCK", value: token },
  { name: "AWS_REGION", value: region }
];

// === 5. 差分生成と適用 ===
const edits = modify(
  text,
  ["claude-code.environmentVariables"],
  envVars,
  { formattingOptions: { insertSpaces: true, tabSize: 2, eol: "\n" } }
);

const newText = applyEdits(text, edits);
writeFileSync(settingsPath, newText, "utf8");

console.log(`✅ Updated ${settingsPath}`);