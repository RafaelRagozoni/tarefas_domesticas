import { useState } from "react";
function AddTask({ tasks, onAddTaskSubmit }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  return (
    <div className="space-y-4 p-6 bg-slate-200 rounded-md shadow">
      <input
        className="border border-slate-300 outline-slate-400 px-4 py-2 rounded w-full"
        type="text"
        placeholder="Digite o titulo da tarefa"
        value={title}
        onChange={(event) => setTitle(event.target.value)}
      />
      <input
        className="border border-slate-300 outline-slate-400 px-4 py-2 rounded w-full"
        type="text"
        placeholder="Digite a descrição da tarefa"
        value={description}
        onChange={(event) => setDescription(event.target.value)}
      />
      <button
        onClick={() => {
          if (!title.trim() || !description.trim()) {
            return alert("Preencha os campos ");
          }
          onAddTaskSubmit(title, description);
        }}
        className="bg-slate-500 text-white px-4 py-2 rounded-md font-medium w-full"
      >
        Adicionar
      </button>
    </div>
  );
}

export default AddTask;
