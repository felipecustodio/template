import { fetchHealth } from "./health.ts";
import "./style.css";

const appRoot = document.querySelector<HTMLElement>("#app");

if (appRoot === null) {
  throw new Error("Missing #app root");
}

const app: HTMLElement = appRoot;

function render(status: string, detail: string): void {
  app.replaceChildren();

  const eyebrow = document.createElement("p");
  eyebrow.className = "eyebrow";
  eyebrow.textContent = "FULL-STACK TEMPLATE";

  const heading = document.createElement("h1");
  heading.textContent = status;

  const message = document.createElement("p");
  message.className = "detail";
  message.textContent = detail;

  app.append(eyebrow, heading, message);
}

render("Checking service", "Waiting for the Robyn API.");

try {
  const health = await fetchHealth();
  render("Ready", `API status: ${health.status}`);
} catch (error: unknown) {
  const detail =
    error instanceof Error ? error.message : "Unknown health error";
  render("Service unavailable", detail);
}
