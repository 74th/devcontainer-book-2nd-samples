import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { homedir } from "node:os";
import { parse, modify, applyEdits } from "jsonc-parser";
import path from "node:path";

const secretPath = "/run/secrets/bedrock_api_key";
const settingsPath = path.join(
  homedir(),
  ".vscode-server/data/Machine/settings.json"
);

// === 1. トークン読み込み ===
if (!existsSync(secretPath)) {
  console.error(`Error: Secret file not found: ${secretPath}`);
  process.exit(1);
}
const token = readFileSync(secretPath, "utf8").trim();

// === 2. 既存設定読み込み ===
let text = "{}";
if (existsSync(settingsPath)) {
  text = readFileSync(settingsPath, "utf8");
}

const json = parse(text, [], { allowTrailingComma: true, disallowComments: false }) ?? {};

// === 3. claude-code.environmentVariables を更新 ===
const envVars = [
  { name: "CLAUDE_CODE_USE_BEDROCK", value: "1" },
  { name: "AWS_BEARER_TOKEN_BEDROCK", value: token },
  { name: "AWS_REGION", value: "ap-northeast-1" }
];

// JSONC 上書き差分作成
const edits = modify(
  text,
  ["claude-code.environmentVariables"],
  envVars,
  { formattingOptions: { insertSpaces: true, tabSize: 2, eol: "\n" } }
);

// === 4. 差分適用して上書き ===
const newText = applyEdits(text, edits);
writeFileSync(settingsPath, newText, "utf8");

console.log(`✅ Updated ${settingsPath}`);