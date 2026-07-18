# -*- coding: utf-8 -*-
"""
insananalitigi
==============

Craig Starbuck'ın *"The Fundamentals of People Analytics: With Applications
in R"* kitabına eşlik eden R **peopleanalytics** (v0.1.0) veri paketinin
**Türkçeleştirilmiş** Python sürümü.

12 veri seti; sütun adları ve kategorik değerler Türkçeye çevrilmiş olarak
:class:`pandas.DataFrame` biçiminde sunulur.

Temel kullanım
--------------
>>> import insananalitigi as ia
>>> ia.veri_setleri()
['anket_yanitlari', 'bordro', 'calisanlar', ...]
>>> df = ia.yukle("calisanlar")
>>> df = ia.calisanlar()            # kısayol fonksiyonu
>>> print(ia.acikla("calisanlar"))  # Türkçe değişken açıklamaları

Lisans: MIT (orijinal paketle aynı).
"""

from __future__ import annotations

import json
from functools import lru_cache
from importlib import resources

import pandas as pd

__version__ = "0.1.0"
__author__ = "Craig Starbuck (orijinal R paketi); Türkçe Python portu"

_VERI_SETLERI = (
    "anket_yanitlari",
    "bordro",
    "calisanlar",
    "demografi",
    "devir_egilimleri",
    "durum",
    "is_bilgileri",
    "kidem",
    "onceki_istihdam",
    "performans",
    "tutum",
    "yan_haklar",
)

__all__ = ["veri_setleri", "yukle", "acikla", "tumunu_yukle", *_VERI_SETLERI]


def _veri_yolu(dosya: str):
    return resources.files(__package__).joinpath("data", dosya)


def veri_setleri() -> list[str]:
    """Mevcut tüm veri setlerinin adlarını döndürür."""
    return list(_VERI_SETLERI)


@lru_cache(maxsize=None)
def _dokumantasyon() -> dict[str, str]:
    with _veri_yolu("veri_seti_dokumantasyonu.json").open(encoding="utf-8") as f:
        return json.load(f)


def acikla(ad: str) -> str:
    """Bir veri setinin Türkçe dokümantasyonunu (değişken açıklamaları) döndürür.

    Parametreler
    ------------
    ad : str
        :func:`veri_setleri` içindeki adlardan biri.
    """
    _dogrula(ad)
    return _dokumantasyon()[ad]


def _dogrula(ad: str) -> None:
    if ad not in _VERI_SETLERI:
        raise KeyError(
            f"Bilinmeyen veri seti: {ad!r}. Mevcut olanlar: {', '.join(_VERI_SETLERI)}"
        )


@lru_cache(maxsize=None)
def _onbellekten_yukle(ad: str) -> pd.DataFrame:
    with _veri_yolu(f"{ad}.csv").open(encoding="utf-8-sig") as f:
        return pd.read_csv(f)


def yukle(ad: str, kopya: bool = True) -> pd.DataFrame:
    """Bir veri setini :class:`pandas.DataFrame` olarak yükler.

    Parametreler
    ------------
    ad : str
        :func:`veri_setleri` içindeki adlardan biri.
    kopya : bool, varsayılan True
        Yerinde (in-place) değişikliklerin önbelleği bozmaması için
        savunmacı bir kopya döndürür.
    """
    _dogrula(ad)
    df = _onbellekten_yukle(ad)
    return df.copy() if kopya else df


def tumunu_yukle(kopya: bool = True) -> dict[str, pd.DataFrame]:
    """Tüm veri setlerini yükler; ``{ad: DataFrame}`` sözlüğü döndürür."""
    return {ad: yukle(ad, kopya=kopya) for ad in _VERI_SETLERI}


def _erisimci_uret(ad: str):
    def _erisimci(kopya: bool = True) -> pd.DataFrame:
        return yukle(ad, kopya=kopya)

    _erisimci.__name__ = ad
    _erisimci.__qualname__ = ad
    _erisimci.__doc__ = (
        f"``{ad}`` veri setini pandas DataFrame olarak yükler.\n\n"
        f"``yukle({ad!r})`` ile eşdeğerdir. Değişken açıklamaları için "
        f"``acikla({ad!r})`` kullanın."
    )
    return _erisimci


for _ad in _VERI_SETLERI:
    globals()[_ad] = _erisimci_uret(_ad)
del _ad
