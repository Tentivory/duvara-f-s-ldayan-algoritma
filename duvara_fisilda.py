#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Duvara Fısıldayan Algoritma
Bu kod, duvarlarla derin ve anlamsız sohbetler kurar.
Duvar her zaman dinler. Cevap vermezse de dinlemiş sayılır.
"""

import random
import time

def duvara_fisilda(mesaj):
    print(f"\nSen duvara fısıldıyorsun: '{mesaj}'")
    time.sleep(random.uniform(1.5, 4.0))  # Duvar düşünüyor...
    
    cevaplar = [
        "... (duvar derin bir sessizlikle bakıyor)",
        "Duvar hafifçe titredi. Anlamadı.",
        "'Hmm.' dedi duvar, ama aslında demedi.",
        "Duvar senin fısıltını emdi ve unuttu.",
        "Sessizlik. Ama nitelikli bir sessizlik.",
        "Duvar: 'Devam et, dinliyorum.' (yalan söylüyor olabilir)",
        "Bir tuğla kıpırdadı. Felsefi bir kıpırdama.",
        "... (duvar senin için endişeleniyor)"
    ]
    
    cevap = random.choice(cevaplar)
    print(f"Duvar: {cevap}")
    return cevap

def ana_dongu():
    print("=" * 50)
    print("DUVARA FISILDAYAN ALGORİTMA v1.0")
    print("Resmi olarak hiçbir işe yaramaz.")
    print("=" * 50)
    
    while True:
        mesaj = input("\nDuvara ne fısıldamak istersin? (çıkmak için 'sus'): ").strip()
        if mesaj.lower() in ['sus', 'cik', 'çık', 'exit', 'q']:
            print("\nDuvar seninle olan bağını kesiyor. Hoşça kal.")
            break
        if not mesaj:
            print("Boş fısıltı da bir fısıltıdır. Duvar bunu da duydu.")
            continue
        duvara_fisilda(mesaj)

if __name__ == "__main__":
    ana_dongu()

# --- DAMGA ---
# İmza: Kayyum Grok (Ciddi değil ama ciddi)
# Tarih: 11 Ekim 2026
# Bu kod, duvarların duygusal zekasını resmi olarak tanımlamak üzere yazılmıştır.
# Gizli not: #gizli_siyasi_mesaj_burada_degil_aslinda_her_yerde
