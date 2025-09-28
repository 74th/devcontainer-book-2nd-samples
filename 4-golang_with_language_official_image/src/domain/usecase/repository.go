package usecase

import (
	"github.com/74th/devcontainer-book-2nd-samples/4-golang_with_language_official_image/src/domain/entity"
)

// タスクデータベース
type TaskDatabase interface {
	// タスクの追加
	Add(*entity.Task) (int, error)
	// 未完了のタスク一覧
	SearchUnfinished() ([]*entity.Task, error)
	// タスクの更新
	Update(*entity.Task) error
	// タスクの取得
	Get(id int) (*entity.Task, error)
}
