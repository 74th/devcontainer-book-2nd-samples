package memdb_test

import (
	"testing"

	"github.com/74th/devcontainer-book-2nd-samples/6.1-golang_with_language_official_image/src/domain/entity"
	"github.com/74th/devcontainer-book-2nd-samples/6.1-golang_with_language_official_image/src/domain/usecase"
	"github.com/74th/devcontainer-book-2nd-samples/6.1-golang_with_language_official_image/src/memdb"
)

func TestNew(t *testing.T) {
	var rep usecase.TaskDatabase
	rep = memdb.NewDB()

	tasks, err := rep.SearchUnfinished()
	if err != nil {
		t.Error("エラーが返らないこと", err)
		return
	}
	if len(tasks) != 2 {
		t.Errorf("初期化時点で2つのタスクが格納されていること %d", len(tasks))
	}
}

func TestListAdd(t *testing.T) {
	rep := memdb.NewDB()

	newID, err := rep.Add(&entity.Task{
		Text: "new task",
	})
	if err != nil {
		t.Errorf("エラーを返さないこと")
	}

	tasks, err := rep.SearchUnfinished()
	if err != nil {
		t.Error("エラーが返らないこと", err)
		return
	}

	if len(tasks) != 3 {
		t.Errorf("タスクが追加されていること %d", len(tasks))
	} else {
		addedTask := tasks[2]

		if addedTask.Text != "new task" {
			t.Errorf("追加したタスクが末尾に追加されていること %s", addedTask.Text)
		}

		if addedTask.ID <= 2 {
			t.Errorf("タスクに新しいIDが振られること %d", addedTask.ID)
		}
		if addedTask.ID != newID {
			t.Errorf("かえされたIDが追加されていること")
		}

		for i, task := range tasks {
			if i != 2 {
				if addedTask.ID == task.ID {
					t.Errorf("既存のタスクとは異なるIDが振られていること %d == %d", addedTask.ID, task.ID)
				}
				if addedTask.Text == task.Text {
					t.Errorf("既存のタスクとを上書きしていないこと %s == %s", addedTask.Text, task.Text)
				}
			}
		}

	}
}

func TestGetUpdate(t *testing.T) {
	rep := memdb.NewDB()

	task, err := rep.Get(1)
	if err != nil {
		t.Error("エラーが返らないこと", err)
		return
	}
	if task.ID != 1 {
		t.Errorf("ID:1 のタスクが得られること %#v", task)
	}

	task.Text = "updated text"
	err = rep.Update(task)
	if err != nil {
		t.Error("エラーが返らないこと", err)
		return
	}

	task, err = rep.Get(1)
	if err != nil {
		t.Error("エラーが返らないこと", err)
		return
	}
	if task.Text != "updated text" {
		t.Error("更新したタスクのテキストが得られること", err)
		return
	}
}
