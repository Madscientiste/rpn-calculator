import { ChangeEvent, useState } from "react";

import { ExclamationTriangleIcon } from "@heroicons/react/24/outline";
import { Alert, Stack, Text, TextInput, ThemeIcon } from "@mantine/core";

import { Result, getResult } from "../api/getResult";

const timeoutTable = new Map<string, number>();

export function ExpressionInput() {
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
					const body: Result = await res.json();

					if (res.status !== 200) {
						throw new Error(body.detail);
					}

					setResult(body);
					setError(null);
				})
				.catch((err) => {
					setError(err);
					setResult(null);
				});
		}, 300);

		timeoutTable.set("expression", id);
	};

	return (
		<Stack gap={4}>
			<TextInput
				style={{ fontFamily: "'Multi', sans-serif" }}
				onChange={handleInput}
				error={!!error}
				rightSection={
					error && (
						<ThemeIcon size="md" variant="subtle" c="red">
							<ExclamationTriangleIcon />
						</ThemeIcon>
					)
				}
				placeholder="5 5 8 * +"
				label="Expression"
			/>
			{result && (
				<Alert color="indigo.3">
					<Text c="indigo.9" fw="bolder" size="sm">
						{result ? result.result : "No result yet"}
					</Text>
				</Alert>
			)}
			{error && (
				<Alert color="red">
					<Text c="red.9" fw="bolder" size="sm">
						{error.message}
					</Text>
				</Alert>
			)}
		</Stack>
	);
}
