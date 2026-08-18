export function downloadTextFile({
    filename = "mol-analysis.txt",
    content = ""
  }) {
    const blob = new Blob([content], {
      type: "text/plain;charset=utf-8"
    });
  
    const url = URL.createObjectURL(blob);
  
    const link = document.createElement("a");
  
    link.href = url;
    link.download = filename;
  
    document.body.appendChild(link);
    link.click();
  
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  }
  
  
  export function analysisToText(item) {
    if (!item) return "";
  
    const lines = [
      "MOON ONYX LABS",
      item.toolName || "Executive Insight Engine",
      "",
      item.title || "Saved Analysis",
      item.status ? `Status: ${item.status}` : "",
      item.createdAt
        ? `Created: ${new Date(item.createdAt).toLocaleString()}`
        : "",
      "",
      "ORIGINAL INPUT",
      "--------------",
      item.input || "No original input stored.",
      "",
      "ANALYSIS RESULT",
      "---------------"
    ];
  
    const result = item.result || {};
  
    switch (item.toolId) {
      case "clarity":
        lines.push(
          `Clarity Score: ${result.score ?? "—"}/100`,
          `Status: ${result.label ?? "—"}`,
          "",
          "Recommendation:",
          result.recommendation || "",
          "",
          "Refined Executive Copy:",
          result.refined_text || ""
        );
        break;
  
      case "kpi-cleaner":
        lines.push(
          `Issues Found: ${result.issues_found ?? "—"}`,
          `Status: ${result.label ?? "—"}`,
          "",
          result.result || ""
        );
        break;
  
      case "insights":
        lines.push(
          `Insight Type: ${result.insight_type ?? "—"}`,
          "",
          "Primary Insight:",
          result.primary_insight || "",
          "",
          "So What?",
          result.so_what || "",
          "",
          "Recommended Action:",
          result.recommended_action || "",
          "",
          "Executive Title:",
          result.executive_title || "",
          "",
          "Chart Suggestion:",
          result.chart_suggestion || ""
        );
        break;
  
      case "dashboard":
        lines.push(
          `Performance Status: ${result.performance_status ?? "—"}`,
          "",
          "Executive Summary:",
          result.executive_summary || "",
          "",
          "Performance Drivers:",
          result.performance_drivers || "",
          "",
          "Risks & Watch Items:",
          result.risks || "",
          "",
          "Recommended Action:",
          result.recommended_action || "",
          "",
          "Outlook:",
          result.outlook || ""
        );
        break;
  
      case "executive-memo":
        lines.push(
          result.title || item.title || "Executive Memo",
          "",
          "Executive Summary:",
          result.summary || "",
          "",
          "Background:",
          result.background || "",
          "",
          "Key Findings:",
          result.findings || "",
          "",
          "Business Impact:",
          result.impact || "",
          "",
          "Recommendations:",
          result.recommendations || "",
          "",
          "Next Steps:",
          result.next_steps || ""
        );
        break;
  
      case "kpi-health":
        lines.push(
          `Overall Health Score: ${result.overall_score ?? "—"}/100`,
          "",
          "Executive Assessment:",
          result.summary || "",
          "",
          "Strengths:",
          ...(result.strengths ?? []).map((item) => `- ${item}`),
          "",
          "Concerns:",
          ...(result.concerns ?? []).map((item) => `- ${item}`),
          "",
          "Recommendations:",
          ...(result.recommendations ?? []).map((item) => `- ${item}`)
        );
        break;
  
      default:
        lines.push(JSON.stringify(result, null, 2));
    }
  
    return lines
      .filter((line) => line !== undefined)
      .join("\n");
  }
  
  
  export function exportAnalysisAsText(item) {
    const safeTitle =
      (item?.title || "mol-analysis")
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, "-")
        .replace(/^-|-$/g, "");
  
    downloadTextFile({
      filename: `${safeTitle || "mol-analysis"}.txt`,
      content: analysisToText(item)
    });
  }