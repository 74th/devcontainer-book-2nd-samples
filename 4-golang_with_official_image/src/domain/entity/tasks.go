package entity

// Task タスク
type Task struct {
	ID   int    `json:"id,omitempty"`
	Text string `json:"text,omitempty"`
	Done bool   `json:"done,omitempty"`
}

func (t Task) Clone() *Task {
	return &t
}
