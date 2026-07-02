const API_BASE = "http://127.0.0.1:8000";

export async function apiPost(endpoint, payload) {
    const response = await fetch(`${API_BASE}${endpoint}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    });

    if (!response.ok) {
        throw new Error("Backend error");
    }

    return response.json();
}