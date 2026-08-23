import { supabase } from './supabaseClient.js';

export async function saveAnalysisToCloud({
  toolId,
  title,
  input,
  result
}) {
  const {
    data: { user },
    error: userError
  } = await supabase.auth.getUser();

  if (userError) {
    throw userError;
  }

  if (!user) {
    throw new Error('You must be signed in to save an analysis.');
  }

  const { data, error } = await supabase
    .from('analyses')
    .insert({
      user_id: user.id,
      tool_id: toolId,
      title,
      input_data: input ?? {},
      result_data: result ?? {}
    })
    .select()
    .single();

  if (error) {
    throw error;
  }

  return data;
}


export async function getCloudAnalyses() {
  const { data, error } = await supabase
    .from('analyses')
    .select('*')
    .order('created_at', {
      ascending: false
    });

  if (error) {
    throw error;
  }

  return data ?? [];
}


export async function deleteCloudAnalysis(id) {
  const { error } = await supabase
    .from('analyses')
    .delete()
    .eq('id', id);

  if (error) {
    throw error;
  }

  return id;
}

export async function clearCloudAnalyses() {
  const {
    data: { user },
    error: userError
  } = await supabase.auth.getUser();

  if (userError) {
    throw userError;
  }

  if (!user) {
    throw new Error(
      'You must be signed in to clear your Workspace.'
    );
  }

  const { error } = await supabase
    .from('analyses')
    .delete()
    .eq('user_id', user.id);

  if (error) {
    throw error;
  }

  return [];
}