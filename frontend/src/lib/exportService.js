const API_BASE = 'http://127.0.0.1:8000';

export async function exportAnalysisPDF(analysis) {
  const response = await fetch(`${API_BASE}/exports/pdf`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(analysis)
  });

  if (!response.ok) {
    let message = 'Unable to export PDF.';

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

  const disposition =
    response.headers.get('content-disposition');

  let filename = 'mol-analysis.pdf';

  if (disposition) {
    const match = disposition.match(
      /filename="?([^"]+)"?/i
    );

    if (match?.[1]) {
      filename = match[1];
    }
  }

  const url = URL.createObjectURL(blob);

  const link = document.createElement('a');

  link.href = url;
  link.download = filename;

  document.body.appendChild(link);

  link.click();
  link.remove();

  URL.revokeObjectURL(url);

  return filename;
}