type THistoryProps = {
	history: {
		expression: string;
		result: string;
	}[];
};

export function HistoryPanel({ history }: THistoryProps) {
	const handleExport = () => {};

	return (
		<div className="history-panel">
			<div className="panel-header">
				<h2>History</h2>
				<button className="export" onClick={handleExport}>
					Export
				</button>
			</div>

			<div className="panel-history">
				{history.map((item, index) => (
					<div key={index} className="history-item">
						<p className="expression">{item.expression}</p>
						<p className="result">{item.result}</p>
					</div>
				))}

				{history.length === 0 && (
					<div className="history-item">
						<p className="expression">No history yet</p>
					</div>
				)}
			</div>
		</div>
	);
}
