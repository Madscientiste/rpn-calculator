import { Accordion, Alert, Stack, Text } from "@mantine/core";

export function HowDoesItWork() {
	return (
		<Accordion>
			<Accordion.Item value="details">
				<Accordion.Control>
					<Text size="xs" fw="bold" c="gray.7">
						How does it work?
					</Text>
				</Accordion.Control>

				<Accordion.Panel>
					<Stack>
						<Text size="xs" c="gray.7">
							An RPN calculator operates on a stack. It holds operands on this stack until an operator is encountered.
							At that time, the appropriate number of operands are popped off the stack, the operation is carried out,
							and the result is pushed back onto the stack.
						</Text>

						<Alert color="indigo" title="Note">
							<Text size="xs" c="indigo.9" fw="bold">
								It can also be implemented using a binary tree, but i've chosen to use a stack.
							</Text>
						</Alert>
					</Stack>
				</Accordion.Panel>
			</Accordion.Item>
		</Accordion>
	);
}
