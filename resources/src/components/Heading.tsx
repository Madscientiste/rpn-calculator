import { Stack, Text, Title } from "@mantine/core";

export function Heading() {
	return (
		<Stack gap={4}>
			<Title order={2} c="gray.9">
				Reverse Łukasiewicz Notation Calculator
			</Title>

			<Text size="sm" fw="bolder" c="gray.7">
				Reverse Polish notation, also known as Polish postfix notation or simply postfix notation, is a mathematical
				notation in which operators follow their operands, in contrast to Polish notation (PN), in which operators
				precede their operands. It does not need any parentheses as long as each operator has a fixed number of
				operands.
			</Text>
		</Stack>
	);
}
