package memdb

import (
	"errors"
	"fmt"

	"github.com/74th/devcontainer-book-2nd-samples/4-golang_with_language_official_image/src/domain/entity"
	"github.com/74th/devcontainer-book-2nd-samples/4-golang_with_language_official_image/src/domain/usecase"
)

var ErrNotFound = errors.New("Not found")

// タスクデータベースの実装
type Instance struct {
	tasks []entity.Task
}

// タスクの追加
func (s *Instance) Add(task *entity.Task) (int, error) {
	task.ID = len(s.tasks) + 1
	s.tasks = append(s.tasks, *task)
	return task.ID, nil
}

// 未完了のタスクの検索
func (s *Instance) SearchUnfinished() ([]*entity.Task, error) {
	result := []*entity.Task{}
	for _, task := range s.tasks {
		if !task.Done {
			result = append(result, task.Clone())
		}
	}
	return result, nil
}

// Update タスクを更新にする
func (s *Instance) Update(task *entity.Task) error {
	for i, currentTask := range s.tasks {
		if currentTask.ID == task.ID {
			s.tasks[i] = *task
			return nil
		}
	}

	return fmt.Errorf("%w id:%d", ErrNotFound, task.ID)
}

// Get タスクを取得する
func (s *Instance) Get(id int) (*entity.Task, error) {
	for i, task := range s.tasks {
		if task.ID == id {
			s.tasks[i].Done = true
			return task.Clone(), nil
		}
	}
	return nil, nil
}

// インスタンスの作成
func NewDB() usecase.TaskDatabase {
	s := new(Instance)
	s.tasks = make([]entity.Task, 2, 20)
	s.tasks[0] = entity.Task{
		ID:   1,
		Text: "task1",
		Done: false,
	}
	s.tasks[1] = entity.Task{
		ID:   2,
		Text: "task2",
		Done: false,
	}

	return s
}
