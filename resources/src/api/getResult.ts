export type Payload = {
	expression: string;
};

export type Result = {
	expression: string;
	result: string;
	detail?: string;
};

export function getResult(payload: Payload): Promise<Response> {
	return fetch("/api/calc", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(payload),
	});
}
