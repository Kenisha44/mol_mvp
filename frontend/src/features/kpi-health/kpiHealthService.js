import { apiPost } from "../../lib/api.js";

export async function analyzeKPIHealth(payload) {
    return apiPost("/kpi-health/analyze", payload);
}