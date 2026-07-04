import { apiPost } from "../../lib/api.js";

export async function generateExecutiveMemo(payload) {
  return apiPost("/executive-memo/generate", payload);
}