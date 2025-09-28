package usecase_test

import (
	"testing"

	"github.com/74th/devcontainer-book-2nd-samples/4-golang_with_official_image/src/domain/entity"
	"github.com/74th/devcontainer-book-2nd-samples/4-golang_with_official_image/src/domain/usecase"
	"github.com/74th/devcontainer-book-2nd-samples/4-golang_with_official_image/src/memdb"
)

func newInteractor() usecase.Interactor {
	return usecase.Interactor{
		Database: memdb.NewDB(),
	}
}

func TestCreateTask(t *testing.T) {
	it := newInteractor()

	tasks, err := it.ShowTasks()
	if err != nil {
		t.Error("エラーが返らないこと")
		return
	}
	if len(tasks) != 2 {
		t.Error("初期状態のリポジトリからはからの2つのタスクが引けること")
		return
	}

	newTask := &entity.Task{
		Text: "task1",
	}

	newTask, err = it.CreateTask(newTask)
	if err != nil {
		t.Error("エラーが返らないこと")
	}
	if newTask.ID == 0 {
		t.Error("タスクIDが割り振られること")
	}

	tasks, err = it.ShowTasks()
	if err != nil {
		t.Error("エラーが返らないこと")
		return
	}
	if len(tasks) != 3 {
		t.Error("初期状態のリポジトリからはからの3つのタスクが引けること")
		return
	}
}

func TestDoneTask(t *testing.T) {
	it := newInteractor()

	tasks, err := it.ShowTasks()
	if err != nil {
		t.Error("エラーが返らないこと")
		return
	}
	if len(tasks) != 2 {
		t.Error("初期状態のリポジトリからはからのタスクが引けること")
		return
	}

	doneTask := tasks[0].ID

	task, err := it.DoneTask(doneTask)
	if err != nil {
		t.Error("エラーが返らないこと")
		return
	}
	if task.Done == false {
		t.Error("完了状態になったタスクが得られること")
		return
	}

	tasks, err = it.ShowTasks()
	if err != nil {
		t.Error("エラーが返らないこと")
		return
	}
	if len(tasks) != 1 {
		t.Error("完了したタスクは返らないこと")
		return
	}
	if tasks[0].ID == doneTask {
		t.Error("完了したタスクは返らないこと")
		return
	}
}
