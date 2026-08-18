const API_BASE_URL = "http://127.0.0.1:8000";


function getFilename(response, fallback) {
  const disposition = response.headers.get("content-disposition");

  if (!disposition) {
    return fallback;
  }

  const match = disposition.match(/filename="?([^"]+)"?/i);

  return match?.[1] || fallback;
}


function downloadBlob(blob, filename) {
  const url = URL.createObjectURL(blob);

  const link = document.createElement("a");

  link.href = url;
  link.download = filename;

  document.body.appendChild(link);

  link.click();
  link.remove();

  URL.revokeObjectURL(url);
}


async function exportAnalysis(endpoint, payload, fallbackFilename) {
  const response = await fetch(
    `${API_BASE_URL}/exports/${endpoint}`,
    {
      method: "POST",

      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify(payload)
    }
  );

  if (!response.ok) {
    let message = `Unable to export ${endpoint.toUpperCase()}.`;

    try {
      const errorData = await response.json();

      message =
        errorData?.detail ||
        errorData?.message ||
        message;
    } catch {
      // Response was not JSON.
    }

    throw new Error(message);
  }

  const blob = await response.blob();

  const filename = getFilename(
    response,
    fallbackFilename
  );

  downloadBlob(blob, filename);

  return filename;
}


export async function exportAnalysisPDF(payload) {
  return exportAnalysis(
    "pdf",
    payload,
    "mol-analysis.pdf"
  );
}


export async function exportAnalysisDOCX(payload) {
  return exportAnalysis(
    "docx",
    payload,
    "mol-analysis.docx"
  );
}