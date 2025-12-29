function getPathway(ageGroup, symptoms) {
    const redFlags = ['severe_chest_pain', 'stroke_signs', 'severe_bleeding', 'difficulty_breathing'];
    if (symptoms.some(s => redFlags.includes(s))) {
        return { 
            message: '<strong>🚨 EMERGENCY</strong><br>This may be serious.<br><strong>Call 999 immediately</strong> or go to A&E.', 
            serviceType: null 
        };
    }

    if (symptoms.includes('sore_throat') && ageGroup !== 'under1') {
        return { message: '<strong>Community Pharmacy (Pharmacy First)</strong><br>Sore throat is eligible for pharmacy consultation and treatment.', serviceType: 'pharmacy' };
    }
    if (symptoms.includes('earache') && ['1-4', '5-11', '12-17'].includes(ageGroup)) {
        return { message: '<strong>Community Pharmacy (Pharmacy First)</strong><br>Earache treatment available for ages 1–17.', serviceType: 'pharmacy' };
    }
    if (symptoms.includes('uti') && ageGroup === '18-64') {
        return { message: '<strong>Community Pharmacy (Pharmacy First)</strong><br>Uncomplicated UTI treatment for women 16–64.', serviceType: 'pharmacy' };
    }
    if (['sinusitis', 'shingles', 'impetigo', 'infected_insect_bite'].some(s => symptoms.includes(s))) {
        return { message: '<strong>Community Pharmacy (Pharmacy First)</strong><br>Your symptom is eligible.', serviceType: 'pharmacy' };
    }
    if (symptoms.includes('minor_cut_sprain')) {
        return { message: '<strong>Urgent Treatment Centre</strong><br>Recommended for minor injuries like cuts or sprains.', serviceType: 'urgent' };
    }
    if (['mild_headache', 'mild_cough'].some(s => symptoms.includes(s))) {
        return { message: '<strong>Self-care recommended</strong><br>Rest, fluids, and over-the-counter remedies. Visit pharmacy if needed.', serviceType: 'pharmacy' };
    }

    return { message: '<strong>GP or NHS 111</strong><br>Book a GP appointment or call 111 for advice.', serviceType: 'gp' };
}