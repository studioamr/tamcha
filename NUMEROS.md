# TAMCHA · Números (modelo auditado)

**Fecha:** 18-ago-2026 · TC usado: 17.06 MXN/USD (FIX Banxico 12-ago-2026).
**Método:** modelo construido SOLO sobre los hallazgos de `INVESTIGACION.md`, luego auditado por dos revisores adversariales (aritmética + realismo vs fuentes). Veredicto de ambos: *con problemas* → **las 14 correcciones ya están aplicadas abajo.** Utilidades pre-ISR/PTU salvo donde se indique.

## Unit economics (por producto)

| Producto | Precio | Costo | Margen | Nota |
|---|--:|--:|--:|---|
| Matcha latte (2 g ceremonial) | $110 | $18 | ~84% | Insumo $12-20/taza; matcha ceremonial $2,700-5,100/kg |
| Espresso | $55 | $8 | ~86% | |
| Anillo plata .925 (China, corregido) | $950 | $400-480 | **50-58%** | La auditoría tumbó el FOB de $8 USD: solo el metal de un anillo de 5-8 g cuesta $165-265 (plata ~$65 USD/oz, ~33 MXN/g en .925). FOB realista $15-18 USD + arancel 25% + IVA + flete |
| Cadena plata .925 (~12 g) | $2,200 | $780 | ~65% | |
| Anillo/cadena de ACERO inoxidable 316L | $450-650 | $40-90 | **~85%** | Línea de entrada (dato nuevo de André 18-ago: la colección también lleva acero). Benchmark: Vitaly vende acero a $50-150 USD; FOB típico $2-5 USD. Estimación propia, cotizar |
| Osito coleccionable | $499 | $150 | ~70% | SUPUESTO propio, sin fuente de costos de peluche custom |

**Regla derivada del superciclo de plata:** markup mínimo 3.5-4x sobre landed y cotizar el metal en vivo en cada pedido.

## CAPEX de apertura — $3,900,000 MXN

| Concepto | MXN |
|---|--:|
| Build-out brutalista ~90 m² (obra $9-18k/m² + 15-30% edificio antiguo) | 1,400,000 |
| Capital de trabajo (3 meses de fijos) — recuperable | 750,000 |
| Equipo de barra (espresso 2 grupos, molino, frío, matcha) | 350,000 |
| Inventario inicial joyería (~350 piezas) | 300,000 |
| Contingencia (8.3% del subtotal de $3.6M — corregido, la nota decía ~9%) | 300,000 |
| Mobiliario + vitrinas con seguridad + LED + POS | 250,000 |
| Depósito + rentas adelantadas (3 × $80k) | 240,000 |
| Inventario accesorios/merch/ositos (supuesto baja confianza) | 120,000 |
| Branding + seeding + evento de apertura | 80,000 |
| Insumos de barra iniciales | 60,000 |
| Permisos y gestoría | 50,000 |

## OPEX mensual — original vs corregido por auditoría

| Concepto | Modelo | Corrección auditoría |
|---|--:|--:|
| Renta + mantenimiento | 88,000 | **121,000-143,000** si es pie de calle real 2026 (los listados de $80k no están confirmados como pie de calle; corredores prime 480-550+/m² y subiendo) |
| Nómina con cargas | 110,000 (6 personas) | **140,000-150,000** (8 personas para 7 días/doble turno: gerente $25-35k, baristas $9-12k + ~30% cargas) |
| COGS bebidas | 60,500 (18%) | **~74,000-84,000** (22-25% blended al incluir el alimento del ticket, que cuesta 35-40%) |
| COGS joyería (28%) | 33,600 | sube si el FOB corregido se confirma (margen 50-58%) |
| COGS merch (35%) | 14,000 | — |
| Marketing continuo | 25,000 | — |
| Servicios | 15,000 | supuesto sin fuente |
| Software/seguros/misc | 12,000 | supuesto sin fuente |
| Comisiones tarjeta ~2.5% | 12,400 | — |
| **Total** | **370,500** | **~445,000-490,000 en el caso duro** |

## Ingresos mensuales (caso base del modelo)

- Bebidas: 70 tickets/día × $160 = $336,000 — ⚠️ la auditoría lo reclasificó como **supuesto de confianza BAJA** (no existe dato público de tráfico); el rango prudente es 50-60 tickets/día → $240,000-288,000.
- Joyería: corregido a **90 piezas/mes** (4% × 2,250 visitas) ≈ $99,000; las "ventas online/destino" extra van aparte como upside, no en el base.
- Merch/coleccionables: $40,000 (8% del total; benchmark 5-15%).

## Escenarios (aritmética corregida)

| Escenario | Ventas/mes | Utilidad/mes (pre-ISR) | Lectura |
|---|--:|--:|---|
| Pesimista (45 tickets, attach 2%) | 249,000 | **−64,000** | El capital de trabajo de $750k aguanta ~11.7 meses de esta sangría sin recortes |
| Base (70 tickets, attach 4%) | 496,000 | **+125,500** | Corregido de 125,000; exige que el supuesto de tráfico se cumpla |
| Optimista (110 tickets, attach 6%, viral tipo SAN/Hema) | 861,000 | **~+400,000** | Recalculado con método único de ratios |
| **Ácido (post-auditoría: 55 tickets, renta $130k, nómina $145k, COGS 24%, margen joyería 55%)** | ~362,000 | **≈ −79,000** | **La flagship pierde dinero si la renta y el tráfico salen al rango corregido** |

## Punto de equilibrio y recuperación

- Break-even: ~$331,000/mes (~$11,040/día). Son **47 tickets/día SI el attach de joyería funciona al 4%** — y **~66 tickets/día solo de cafetería si nadie compra joyería**. Ambos umbrales importan.
- Payback del CAPEX: 31 meses pre-impuestos en base… pero **after-tax (ISR ~30% + PTU 10%) el flujo baja a ~$75-80k/mes → 49-52 meses reales**, más 3-6 meses de ramp-up no modelados. Plan honesto: **40-50+ meses**. En optimista ~10-14; en pesimista nunca.

## Riesgos top (con mitigación)

1. **El attach cafetería→joyería (4%) es el supuesto más frágil y no tiene dato público.** → Validar en pop-up/bazar ANTES de firmar renta (Fases 1-2 de `LANZAMIENTO.md`).
2. **Renta = ~18% de ventas base, el doble de la regla JLL (5-10%).** → No firmar en 2026; negociar post-Mundial; 60-90 m², no 120.
3. **Escasez de matcha** (subasta de tencha ~2x 2025→2026; importación MX +20%). → Contrato anual con proveedor + origen no japonés (coreano) de cobertura.
4. **Superciclo de plata** (~$65 USD/oz, 2.2x vs 2025). → Markup ≥3.5x, precios revisables por drop, y la **línea de acero como cobertura natural**: si la plata sigue subiendo, el acero sostiene el precio de entrada y el margen blended.
5. **Arancel 2026 a importaciones sin tratado (hasta 25% + IVA).** → Confirmar fracción con agente aduanal antes del primer pedido; Taxco como plan B.
6. **Saturación: 179 cafeterías y 8+ matcha bars en la zona.** → La joyería es el corazón; el matcha es la puerta (modelo Kith Treats / Gentle Monster).

## Conclusión (sin maquillaje)

La horquilla del caso base real va de **−$79k a +$125k por mes** dependiendo de dos variables que hoy NADIE conoce: el tráfico real y el attach de joyería. Con $3.9M de CAPEX en juego, abrir flagship directo es apostar a ciegas. El modelo solo aprueba la flagship si antes: (1) el pop-up prueba attach ≥4-8%, (2) se consigue local ≤$90k/mes todo incluido, y (3) el drop online ya genera caja. Eso es exactamente lo que ordena `LANZAMIENTO.md`.
