import { ChangeEvent, useState } from "react";

import "./App.css";
import { HistoryPanel } from "./components/HistoryPanel";
import { Result, getResult } from "./api/getResult";

const timeoutTable = new Map<string, number>();

function App() {
	const [result, setResult] = useState<Result | null>(null);
	const [error, setError] = useState<Error | null>(null);

	// To avoid spamming the api each time the user types a character,
	// i've added a debounce of 300ms to the input.
	const handleInput = async (e: ChangeEvent<HTMLInputElement>) => {
		if (timeoutTable.has("expression")) {
			clearTimeout(timeoutTable.get("expression")!);
		}

		const id = setTimeout(async () => {
			getResult({ expression: e.target.value })
				.then(async (res) => {
					const body = await res.json();
					setResult(body);
				})
				.catch((err) => {
					setError(err);
				});
		}, 300);

		timeoutTable.set("expression", id);
	};

	return (
		<div className="container layout">
			<HistoryPanel history={[]} />

			<div className="calculator stack">
				<div className="inputContainer">
					<input type="text" name="expression" placeholder="expression" onChange={handleInput} />
					<span className="focus-border"></span>
				</div>

				<p className="output">
					{result && result.result}
					{error && error.message}
					{!result && !error && "Result will appear here"}
				</p>
			</div>
		</div>
	);
}

export default App;
