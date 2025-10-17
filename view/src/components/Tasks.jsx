import {
  ChevronDown,
  ChevronDownCircle,
  ChevronFirst,
  ChevronRightIcon,
  DeleteIcon,
  Trash2Icon,
} from "lucide-react";
import { useNavigate } from "react-router-dom";
function Tasks({ tasks, onTaskClick, onDeleteTaskClick }) {
  const navigate = useNavigate(); //trocar de página

  function onSeeDetailsClick(task) {
    const query = new URLSearchParams(); //preparar o path da página
    query.set("title", task.title);
    query.set("description", task.description);
    navigate(`/task?${query.toString()}`);
  }

  function getTasks(task) {
    return (
      <li key={task.id} className="flex gap-2">
        <button
          onClick={() => onTaskClick(task.id)}
          className={`bg-slate-400 w-full text-left text-white p-2 rounded-md ${
            task.isCompleted ? "line-through" : ""
          }`}
        >
          {task.title}
        </button>

        <button
          onClick={() => onSeeDetailsClick(task)}
          className="bg-slate-400 p-2 rounded-md text-white"
        >
          <ChevronRightIcon />
        </button>

        <button
          onClick={() => onDeleteTaskClick(task.id)}
          className="bg-slate-400 p-2 rounded-md text-white"
        >
          <Trash2Icon />
        </button>
      </li>
    );
  }

  return (
    <ul className="space-y-4 p-6 bg-slate-200 rounded-md shadow">
      {tasks.map(getTasks)}
    </ul>
  );
}

export default Tasks;
