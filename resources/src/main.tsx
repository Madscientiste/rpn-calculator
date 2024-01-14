import React from "react";
import ReactDOM from "react-dom/client";

import { MantineProvider, createTheme } from "@mantine/core";

import "@mantine/code-highlight/styles.layer.css";
import "@mantine/core/styles.layer.css";

import App from "./App";

const theme = createTheme({
	fontFamily: "'Merriweather', sans-serif",
});

ReactDOM.createRoot(document.getElementById("root")!).render(
	<React.StrictMode>
		<MantineProvider theme={theme}>
			<App />
		</MantineProvider>
	</React.StrictMode>,
);
