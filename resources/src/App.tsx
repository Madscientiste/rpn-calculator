import { ChangeEvent, useState } from "react";

import "./App.css";

function App() {
	const [expression, setExpression] = useState<null | string>(null);
	const [result, setResult] = useState<null | string>(null);

	const handleInput = async (e: ChangeEvent<HTMLInputElement>) => {
		
	};

	return (
		<div className="wrapper stack">
			<div className="stack">
				<h4>Input</h4>
				<input type="text" value={expression || ""} onChange={handleInput} placeholder="5 8 +" />
			</div>

			<div className="output">
				<h4>Output</h4>
				<div className="content"></div>
			</div>
		</div>
	);
}

export default App;
