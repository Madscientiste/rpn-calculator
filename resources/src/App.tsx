import { Container, Group, Stack } from "@mantine/core";

import "./App.css";

import { ExpressionInput } from "./components/ExpressionInput";
import { Heading } from "./components/Heading";
import { HowDoesItWork } from "./components/HowDoesItWork";

function App() {
	return (
		<Container size="sm" mt="lg">
			<Stack gap={32}>
				<Heading />

				<ExpressionInput />

				<Group grow>
					<HowDoesItWork />
				</Group>
			</Stack>
		</Container>
	);
}

export default App;
