const STORAGE_KEY = "mol_saved_analyses";

export function getSavedAnalyses() {
  try {
    const stored = localStorage.getItem(STORAGE_KEY);

    return stored ? JSON.parse(stored) : [];
  } catch (error) {
    console.error("Could not load saved MOL analyses:", error);
    return [];
  }
}

export function saveAnalysis({
  toolId,
  toolName,
  title,
  status,
  preview,
  input,
  result
}) {
  const analyses = getSavedAnalyses();

  const record = {
    id: crypto.randomUUID(),
    toolId,
    toolName,
    title,
    status,
    preview,
    input,
    result,
    createdAt: new Date().toISOString()
  };

  const updated = [record, ...analyses];

  localStorage.setItem(
    STORAGE_KEY,
    JSON.stringify(updated)
  );

  return record;
}

export function deleteSavedAnalysis(id) {
  const analyses = getSavedAnalyses();

  const updated = analyses.filter(
    (item) => item.id !== id
  );

  localStorage.setItem(
    STORAGE_KEY,
    JSON.stringify(updated)
  );

  return updated;
}

export function clearSavedAnalyses() {
  localStorage.removeItem(STORAGE_KEY);

  return [];
}

export function getSavedAnalysis(id) {
  return getSavedAnalyses().find(
    (item) => item.id === id
  );
}