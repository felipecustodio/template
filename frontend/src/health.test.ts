import { describe, expect, it } from "vitest";

import { healthSchema } from "./health.ts";

describe("healthSchema", () => {
  it("accepts healthy service data", () => {
    expect(healthSchema.parse({ status: "ok" })).toEqual({ status: "ok" });
  });

  it("rejects unknown service status", () => {
    expect(() => healthSchema.parse({ status: "down" })).toThrow();
  });
});
