import { apiPost } from "../../lib/api.js";

export async function generateDashboardNarrative(text) {
    return apiPost("/dashboard-narrative/generate", {
        text
    });
}