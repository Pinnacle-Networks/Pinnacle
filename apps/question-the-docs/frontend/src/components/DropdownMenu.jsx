const DropdownMenu = ({ selectedOption, setSelectedOption }) => {

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };

  return (
    <div>
      <select className="dropdown" value={selectedOption} onChange={handleOptionChange}>
        <option value="">Choose Documentation</option>
        <option value="pinnacledb">SuperDuperDB</option>
        <option value="langchain">LangChain</option>
        <option value="fastchat">FastChat</option>
      </select>
    </div>
  );
};

  export default DropdownMenu;