import { supabase } from './supabaseClient.js';
import {
  profile,
  loadProfile
} from '../stores/profileStore.js';

import { get } from 'svelte/store';


export function getPlanLimits() {
  const currentProfile = get(profile);

  const isPro =
    currentProfile?.plan === 'pro';

  return {
    isPro,
    analysisLimit: isPro ? 100 : 5,
    exportLimit: isPro ? null : 3
  };
}


export function canRunAnalysis() {
  const currentProfile = get(profile);

  if (!currentProfile) {
    return {
      allowed: false,
      reason: 'Unable to load your MOL plan.'
    };
  }

  const {
    isPro,
    analysisLimit
  } = getPlanLimits();

  const currentCount =
    Number(
      currentProfile.analysis_count ?? 0
    );

  if (currentCount >= analysisLimit) {
    return {
      allowed: false,

      reason: isPro
        ? 'You have reached your monthly MOL Pro analysis allowance.'
        : 'You have reached your 5 free analyses for this month.'
    };
  }

  return {
    allowed: true,
    remaining:
      analysisLimit - currentCount
  };
}

export function canExport() {
    const currentProfile = get(profile);
  
    if (!currentProfile) {
      return {
        allowed: false,
        reason: 'Unable to load your MOL plan.'
      };
    }
  
    const {
      isPro,
      exportLimit
    } = getPlanLimits();
  
    // Pro exports are unlimited
    if (isPro) {
      return {
        allowed: true,
        remaining: null
      };
    }
  
    const currentCount =
      Number(
        currentProfile.export_count ?? 0
      );
  
    if (currentCount >= exportLimit) {
      return {
        allowed: false,
        reason:
          'You have reached your 3 free exports for this month.'
      };
    }
  
    return {
      allowed: true,
      remaining:
        exportLimit - currentCount
    };
  }

  export async function recordExportUsage() {
    const currentProfile = get(profile);
  
    if (!currentProfile) {
      throw new Error(
        'Unable to record export usage.'
      );
    }
  
    const nextCount =
      Number(
        currentProfile.export_count ?? 0
      ) + 1;
  
    const { error } = await supabase
      .from('profiles')
      .update({
        export_count: nextCount,
        updated_at: new Date().toISOString()
      })
      .eq('id', currentProfile.id);
  
    if (error) {
      throw error;
    }
  
    await loadProfile();
  
    return nextCount;
  }

export async function recordAnalysisUsage() {
  const currentProfile = get(profile);

  if (!currentProfile) {
    throw new Error(
      'Unable to record analysis usage.'
    );
  }

  const nextCount =
    Number(
      currentProfile.analysis_count ?? 0
    ) + 1;

  const { error } = await supabase
    .from('profiles')
    .update({
      analysis_count: nextCount,
      updated_at: new Date().toISOString()
    })
    .eq('id', currentProfile.id);

  if (error) {
    throw error;
  }

  await loadProfile();

  return nextCount;
}