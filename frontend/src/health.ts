import { z } from "zod";

export const healthSchema = z.object({
  status: z.literal("ok"),
});

export type Health = z.infer<typeof healthSchema>;

export async function fetchHealth(
  request: typeof fetch = fetch,
): Promise<Health> {
  const response = await request("/api/health");

  if (!response.ok) {
    throw new Error(`Health request failed: ${response.status}`);
  }

  return healthSchema.parse(await response.json());
}
