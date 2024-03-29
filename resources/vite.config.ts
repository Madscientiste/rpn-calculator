import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// https://vitejs.dev/config/
export default defineConfig({
	plugins: [react()],

	base: "/calculator",

	server: {
		proxy: {
			"/api": {
				target: "http://localhost:8000",
			},
		},
	},
});
