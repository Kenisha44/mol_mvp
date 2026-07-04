import { apiPost } from "../../lib/api.js";

export async function generateInsight(text) {
    return apiPost("/insights/generate", {
        text
    });
}