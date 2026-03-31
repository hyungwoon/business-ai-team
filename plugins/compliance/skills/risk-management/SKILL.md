---

name: risk-management
description: Identify, assess, and mitigate compliance and operational risks using structured frameworks. Use when conducting risk assessments, building compliance programs, reviewing regulatory requirements, preparing audit responses, or designing internal controls.
version: 2.0.0
last-updated: 2026-03-15
when_to_use: "Use when conducting risk assessments, building compliance programs, reviewing regulatory requirements, preparing audit responses, or designing internal controls."
allowed-tools: [Read, Glob, Grep, WebSearch, WebFetch]
---

# Risk Management Skill

Frameworks for compliance program design, risk assessment, and regulatory adherence in Korean and international business contexts.

## Enterprise Risk Assessment Framework

### Risk Identification Categories

Systematically scan across these risk domains:

| Domain | Key Risk Types |
|---|---|
| **Regulatory / Legal** | Licensing, permits, sector-specific regulations, cross-border compliance |
| **Financial** | Fraud, misstatement, tax non-compliance, sanctions exposure |
| **Operational** | Process failure, vendor dependency, business continuity |
| **Data / Privacy** | Personal data breach, unauthorized processing, cross-border transfer |
| **Reputational** | ESG violations, media exposure, social media incidents |
| **Cybersecurity** | Ransomware, insider threat, third-party breach |
| **HR / Employment** | Wage/hour violations, discrimination, workplace safety |
| **Contractual** | Breach of contract, IP infringement, non-compete violations |

### Risk Scoring Matrix

Rate each identified risk on two dimensions:

**Likelihood** (1–5):
| Score | Label | Frequency |
|---|---|---|
| 1 | Rare | < once every 5 years |
| 2 | Unlikely | Once every 2-5 years |
| 3 | Possible | Once per year |
| 4 | Likely | Several times per year |
| 5 | Almost certain | Monthly or more |

**Impact** (1–5):
| Score | Label | Business Effect |
|---|---|---|
| 1 | Negligible | < ₩10M loss, no external attention |
| 2 | Minor | ₩10-100M loss, internal escalation only |
| 3 | Moderate | ₩100M-1B loss, limited regulatory attention |
| 4 | Major | ₩1-10B loss, regulatory action, media coverage |
| 5 | Critical | > ₩10B loss, criminal liability, license revocation |

**Risk Score = Likelihood × Impact**

| Score | Risk Level | Response |
|---|---|---|
| 1–4 | Low | Monitor, document |
| 5–9 | Medium | Assign owner, quarterly review |
| 10–16 | High | Immediate action plan, monthly review |
| 17–25 | Critical | Escalate to board, external counsel |

---

## Korean Regulatory Compliance

### Key Korean Laws for Business Compliance

| Law | Scope | Penalty Range |
|---|---|---|
| 개인정보 보호법 (PIPA) | Personal data collection, processing, transfer | ₩10-50M fine, 5년 이하 징역 |
| 공정거래법 | Anti-competitive behavior, unfair trade | Revenue-based surcharge up to 10% |
| 전자상거래법 | E-commerce disclosures, refund policies | ₩1-3M fine |
| 근로기준법 | Labor standards, working hours, wage | ₩10-30M fine, 2년 이하 징역 |
| 정보통신망법 | Online privacy, cybersecurity | ₩100M fine, business suspension |
| 중대재해처벌법 | Workplace safety for 50+ employees | CEO criminal liability |
| 공익신고자보호법 | Whistleblower protection | Mandatory reinstatement |

### PIPA Compliance Checklist

- [ ] 개인정보 처리방침 (Privacy Policy) published and current
- [ ] Consent obtained for each purpose of data collection
- [ ] Retention periods defined and enforced
- [ ] Data subject rights process established (열람, 정정, 삭제, 이전)
- [ ] 개인정보보호책임자 (CPO) designated and registered
- [ ] Cross-border transfer agreements in place (for overseas vendors)
- [ ] Breach notification procedure: PIPC within 72 hours
- [ ] Annual internal audit and training completed

---

## Internal Controls Framework

### Control Types

| Control Type | Timing | Example |
|---|---|---|
| **Preventive** | Before the event | Access controls, segregation of duties |
| **Detective** | During or after | Reconciliations, audit trails, anomaly alerts |
| **Corrective** | After detection | Incident response, remediation plans |
| **Directive** | Guiding behavior | Policies, training, code of conduct |

### Segregation of Duties (SoD) — Key Incompatible Functions

| Process | Should NOT be combined |
|---|---|
| Accounts Payable | Invoice approval + payment execution |
| Payroll | Employee setup + payroll processing |
| Procurement | Vendor selection + purchase approval |
| IT | System development + production access |
| Finance | Journal entry + account reconciliation |

### Control Testing Cadence

| Control Risk Level | Testing Frequency | Sample Size |
|---|---|---|
| High | Quarterly | 25 items per quarter |
| Medium | Semi-annual | 15 items per period |
| Low | Annual | 10 items per year |

---

## Compliance Program Design

### Program Pillars (7 Elements — Based on US Sentencing Guidelines / Korean Standards)

1. **Standards and Procedures** — Written policies covering key risk areas
2. **Program Oversight** — Designated compliance officer with board visibility
3. **Training and Education** — Role-based annual training, new hire onboarding
4. **Monitoring and Auditing** — Risk-based audit plan, continuous monitoring tools
5. **Reporting Mechanisms** — Anonymous hotline (신고채널), non-retaliation policy
6. **Enforcement** — Consistent discipline for violations at all levels
7. **Response and Prevention** — Root cause analysis and remediation for incidents

### Compliance Calendar Template

| Month | Activity |
|---|---|
| 1 | Annual risk assessment |
| 2 | Policy review and updates |
| 3 | Q1 control testing |
| 4 | Training completion audit |
| 6 | Q2 control testing + mid-year regulatory scan |
| 9 | Q3 control testing |
| 10 | External audit preparation |
| 12 | Annual compliance report to board |

---

## Incident Response

### Compliance Incident Classification

| Severity | Definition | Response Time | Escalation |
|---|---|---|---|
| P1 | Regulatory breach, criminal exposure | 24 hours | CEO + Board + External counsel |
| P2 | Policy violation with material impact | 72 hours | 임원 + Legal + Compliance |
| P3 | Policy violation, limited impact | 1 week | Department head + Compliance |
| P4 | Minor deviation, self-reported | 1 month | Compliance review only |

### Investigation Checklist

- [ ] Preserve all relevant evidence (documents, emails, system logs)
- [ ] Identify affected parties and scope
- [ ] Determine applicable laws and obligations
- [ ] Engage legal counsel if P1/P2
- [ ] Interview witnesses with counsel present if appropriate
- [ ] Document findings with timeline
- [ ] Implement corrective actions
- [ ] Report to regulators if required
- [ ] Update controls to prevent recurrence

---

## 관련 스킬

| 스킬 | 플러그인 | 관계 |
|------|----------|------|
| legal-risk-assessment | legal | 법적 리스크 평가 (계약, 규제) |
| cybersecurity | security | 사이버보안 리스크 관리 |
| audit-support | finance | 감사 대응 및 내부통제 |

---

## Sector-Specific Compliance Guides

### 핀테크: 전자금융거래법 (Electronic Financial Transactions Act)

Key obligations for fintech companies operating in Korea:

| Requirement | Detail | Penalty for Non-compliance |
|---|---|---|
| 전자금융업 등록 | 금융위원회 등록 필수 (자본금 요건 충족) | 무등록 영업 시 5년 이하 징역 |
| 이용자 보호 | 거래 내역 5년 보관, 분쟁 처리 절차 수립 | ₩10-50M 과태료 |
| 정보보호 | 금융보안원 기준 준수, 연 1회 취약점 점검 | 업무 정지 |
| 이상거래탐지 (FDS) | 실시간 이상거래 탐지 시스템 운영 의무 | 금융감독원 제재 |
| 망분리 | 내부망/외부망 분리 (직원 100인 이상 또는 자산 100억 이상) | 시정 명령 |

**핀테크 컴플라이언스 체크리스트:**
- [ ] 전자금융업 등록 완료 (해당 업종: 전자화폐, 전자자금이체, 결제대행 등)
- [ ] 이용약관 및 개인정보 처리방침 금융위 기준 충족
- [ ] FDS 시스템 구축 및 운영 절차 수립
- [ ] 망분리 요건 충족 여부 확인
- [ ] 금융보안원 FSEC 인증 취득 계획 수립
- [ ] 이용자 피해 보상 절차 및 준비금 확보

### 헬스케어: 의료기기법 (Medical Device Act)

| 등급 | 위험도 | 허가 요건 | 예시 |
|---|---|---|---|
| 1등급 | 낮음 | 신고 (식약처) | 일반 의료용 장갑 |
| 2등급 | 중간 | 인증 (식약처 또는 인증기관) | 혈압계, 체온계 |
| 3등급 | 높음 | 허가 (식약처 직접) | 인공관절, 심장 스텐트 |
| 4등급 | 매우 높음 | 허가 + 임상시험 | 이식형 심박조율기 |

**소프트웨어 의료기기 (SaMD) 주의사항:**
- AI 기반 진단 보조 소프트웨어는 2등급 이상 의료기기로 분류 가능
- 식약처 디지털헬스케어 허가심사 가이드라인 (2023) 적용
- 임상 유효성 데이터 요구 — 국내 임상 또는 해외 임상 + 동등성 입증

**헬스케어 컴플라이언스 체크리스트:**
- [ ] 제품 의료기기 해당 여부 사전 판단 (식약처 사전상담 활용)
- [ ] 등급 분류 및 허가/인증/신고 절차 확인
- [ ] GMP (제조 및 품질관리 기준) 적합 인정 취득
- [ ] 의료기기 UDI (고유기기식별) 등록
- [ ] 부작용 보고 체계 수립 (이상사례 발생 시 15일 이내 보고)

### 교육: 학원법 (Private Teaching Institutes Act)

| 의무 | 내용 | 위반 시 |
|---|---|---|
| 학원 등록 | 시/군/구청 등록 필수 (시설 기준 충족) | 미등록 운영 시 폐쇄 명령 |
| 수강료 게시 | 수강료 및 교습비 공개 게시 의무 | ₩100-500M 과태료 |
| 교습시간 제한 | 심야 교습 금지 (22:00 이후) | 교습 정지 |
| 환불 규정 | 법정 환불 기준 준수 (수강 기간 비례 환불) | 분쟁 조정 + 과태료 |
| 강사 자격 | 과목별 자격 요건 충족 강사 채용 | 시정 명령 |

**에듀테크 플랫폼 추가 고려사항:**
- 온라인 교육 플랫폼은 학원법 적용 여부 사전 확인 필요 (콘텐츠 제공 vs. 교습 행위 구분)
- 아동 대상 서비스: 아동·청소년 개인정보 보호 강화 요건 적용 (법정대리인 동의)

---

## ISMS-P 인증 요구사항 체크리스트

ISMS-P (정보보호 및 개인정보보호 관리체계)는 한국인터넷진흥원(KISA)이 운영하는 인증 제도입니다. 의무 대상: 정보통신서비스 매출 100억 이상 또는 일평균 이용자 100만 명 이상.

### 관리체계 수립 및 운영 (16개 항목)

- [ ] 1.1 경영진의 참여 — 최고경영자 정보보호 방침 승인 및 공표
- [ ] 1.2 최고책임자 지정 — CISO 및 CPO 지정 (겸직 가능 여부 확인)
- [ ] 1.3 조직 구성 — 정보보호 조직 및 역할 정의
- [ ] 1.4 범위 설정 — 인증 범위 문서화 (서비스, 시스템, 조직)
- [ ] 1.5 정책 수립 — 정보보호 정책 및 시행 세칙 수립
- [ ] 1.6 자원 할당 — 정보보호 예산 및 인력 확보
- [ ] 1.7 위험 관리 — 연 1회 이상 위험 평가 수행
- [ ] 1.8 보호대책 구현 — 위험 처리 계획 수립 및 이행
- [ ] 1.9 법적 요구사항 준수 — 관련 법령 목록 관리
- [ ] 1.10 성과 측정 — 정보보호 목표 및 KPI 설정
- [ ] 1.11 이해관계자 소통 — 내부 공유 및 외부 공시
- [ ] 1.12 관리체계 검토 — 경영진 검토 연 1회 이상
- [ ] 1.13 지속적 개선 — 부적합 사항 시정 조치
- [ ] 1.14 내부 감사 — 연 1회 이상 내부 감사 수행
- [ ] 1.15 문서 관리 — 정책/절차 문서 버전 관리
- [ ] 1.16 기록 관리 — 활동 증적 보관 (최소 3년)

### 보호대책 요구사항 (64개 항목 — 주요 항목)

**인적 보안:**
- [ ] 임직원 보안 서약서 징구
- [ ] 연 1회 이상 정보보호 교육 실시
- [ ] 퇴직자 접근 권한 즉시 회수

**접근 통제:**
- [ ] 최소 권한 원칙 적용
- [ ] 특권 계정 관리 (별도 승인 절차)
- [ ] 외부 접속 시 VPN 또는 동등 수준 보안 적용

**암호화:**
- [ ] 개인정보 저장 시 암호화 (AES-256 이상)
- [ ] 전송 구간 암호화 (TLS 1.2 이상)
- [ ] 암호키 관리 절차 수립

**개인정보 처리 단계별 보호 (ISMS-P 추가 항목):**
- [ ] 개인정보 수집 시 동의 절차 적정성
- [ ] 개인정보 보유 기간 준수 및 파기 절차
- [ ] 개인정보 처리 위탁 계약 및 관리 감독

---

## Third-Party Risk Management (TPRM) Framework

### Vendor Risk Tiering

Classify all vendors before onboarding:

| Tier | Criteria | Due Diligence Level |
|---|---|---|
| **Critical** | Access to production systems or personal data of > 10,000 users | Full assessment + annual re-assessment |
| **High** | Access to internal systems or sensitive data | Standard assessment + biennial re-assessment |
| **Medium** | Access to non-sensitive internal data | Questionnaire only + triennial review |
| **Low** | No system access (e.g., office supplies) | Contract review only |

### TPRM Assessment Questionnaire (Critical Vendors)

**Security posture:**
- [ ] ISO 27001 or SOC 2 Type II certification current?
- [ ] Penetration testing conducted annually?
- [ ] Incident response plan documented and tested?
- [ ] Subcontractor / fourth-party risk managed?

**Data handling:**
- [ ] Data processing agreement (DPA) signed?
- [ ] Data residency location confirmed (Korea / overseas)?
- [ ] Cross-border transfer mechanism in place (PIPA Article 28-8)?
- [ ] Data deletion / return procedure on contract termination?

**Business continuity:**
- [ ] BCP/DR plan documented?
- [ ] RTO and RPO defined and tested?
- [ ] Key personnel dependency identified?

**Financial stability:**
- [ ] Financial statements reviewed (for critical vendors)?
- [ ] Concentration risk assessed (single-vendor dependency)?

### Vendor Monitoring Schedule

| Tier | Ongoing Monitoring | Re-assessment |
|---|---|---|
| Critical | Quarterly security questionnaire + news monitoring | Annual |
| High | Semi-annual check-in | Biennial |
| Medium | Annual questionnaire | Triennial |
| Low | Contract renewal review only | As needed |

---

## Anti-Corruption Framework (김영란법 / 부정청탁방지법)

### 부정청탁 및 금품등 수수의 금지에 관한 법률 — 핵심 기준

적용 대상: 공직자, 언론인, 사립학교 교직원 및 그 배우자

**금품 수수 허용 한도 (2024년 기준):**

| 구분 | 허용 한도 | 비고 |
|---|---|---|
| 음식물 | 3만원 이하 | 직무 관련성 무관 |
| 선물 | 5만원 이하 (농수산물·가공품 15만원) | 명절 기간 농수산물 상향 적용 |
| 경조사비 | 5만원 이하 (화환·조화 10만원) | 축의금·조의금 포함 |
| 강의료 등 | 시간당 40만원 이하 (외부 강의) | 사전 신고 의무 |

**부정청탁 금지 행위 (14개 유형 — 주요 항목):**
- 인허가, 면허, 특허 등 행정처분 관련 청탁
- 수사, 재판, 심판 관련 청탁
- 채용, 승진, 전보 등 인사 관련 청탁
- 입찰, 계약 관련 청탁
- 보조금, 지원금 배정 관련 청탁

### 기업 내부 컴플라이언스 절차

```
외부 접대/선물 제공 프로세스:

1. 사전 승인
   - 공직자 대상 접대/선물 시 컴플라이언스팀 사전 승인
   - 승인 요청서: 대상자 직위, 목적, 금액, 날짜

2. 한도 확인
   - 음식물 3만원 / 선물 5만원 / 경조사비 5만원 준수
   - 연간 누적 한도 관리 (동일인 대상)

3. 사후 기록
   - 영수증 보관 (5년)
   - 지출 내역 시스템 등록

4. 위반 시 처리
   - 자진 신고 시 감경 가능
   - 은폐 시 가중 처벌
```

---

## Compliance Maturity Model (Level 1-5)

### 성숙도 수준 정의

| Level | 명칭 | 특징 | 주요 지표 |
|---|---|---|---|
| **1 — Initial** | 임시방편 | 컴플라이언스 활동이 비정형적, 개인 의존 | 정책 문서 없음, 사후 대응만 |
| **2 — Developing** | 기초 수립 | 핵심 정책 존재, 일부 프로세스 문서화 | 기본 정책 수립, 연 1회 교육 |
| **3 — Defined** | 체계화 | 표준화된 프로세스, 역할 명확, 정기 감사 | 위험 평가 연 1회, 통제 테스트 |
| **4 — Managed** | 측정 기반 | KPI 추적, 데이터 기반 의사결정, 예방적 관리 | 대시보드 운영, 실시간 모니터링 |
| **5 — Optimizing** | 지속 개선 | 자동화, 예측적 리스크 관리, 업계 벤치마크 선도 | AI 기반 이상 탐지, 외부 인증 다수 |

### 성숙도 향상 로드맵

```
현재 수준 진단 → 목표 수준 설정 → 갭 분석 → 개선 계획

Level 1 → 2 (3-6개월):
  - 핵심 정책 3개 수립 (정보보호, 윤리강령, 개인정보)
  - 컴플라이언스 담당자 지정
  - 신입 교육 프로그램 도입

Level 2 → 3 (6-12개월):
  - 연간 위험 평가 프로세스 수립
  - 내부 감사 계획 수립 및 실행
  - 신고 채널 (익명 핫라인) 구축

Level 3 → 4 (12-24개월):
  - 컴플라이언스 KPI 대시보드 구축
  - 자동화 모니터링 도구 도입
  - 이사회 정기 보고 체계 수립

Level 4 → 5 (24개월+):
  - AI/ML 기반 이상 거래 탐지
  - 외부 인증 취득 (ISMS-P, ISO 37001)
  - 업계 컴플라이언스 포럼 참여 및 기여
```

---

## Compliance Monitoring Dashboard KPIs

### 핵심 컴플라이언스 지표

| KPI | 정의 | 목표 | 측정 주기 |
|---|---|---|---|
| 정책 교육 이수율 | 교육 완료 직원 / 전체 직원 | > 95% | 분기 |
| 위험 평가 완료율 | 평가 완료 리스크 / 식별 리스크 | 100% | 연간 |
| 통제 테스트 통과율 | 통과 통제 / 전체 테스트 통제 | > 90% | 분기 |
| 인시던트 평균 해결 시간 | 인시던트 발생 → 종결 (일) | P1 < 3일, P2 < 7일 | 월간 |
| 미해결 고위험 이슈 | 30일 이상 미해결 고위험 항목 수 | 0 | 주간 |
| 공급업체 평가 완료율 | 평가 완료 공급업체 / 평가 대상 | > 90% | 연간 |
| 내부 신고 건수 | 신고 채널 접수 건수 | 추세 모니터링 | 월간 |
| 규제 변경 대응 시간 | 규제 발효 → 내부 정책 반영 (일) | < 90일 | 건별 |

---

## Regulatory Change Management Process

### 규제 변경 모니터링 체계

```
1. 모니터링 소스 설정
   - 법제처 국가법령정보센터 (law.go.kr) RSS 구독
   - 금융감독원 / 개인정보보호위원회 / 공정거래위원회 공지 구독
   - 법무법인 뉴스레터 구독 (해당 업종 전문)
   - 업종별 협회 규제 동향 보고서

2. 변경 영향 평가 (Change Impact Assessment)
   - 변경 내용 요약
   - 당사 적용 여부 판단
   - 영향 받는 프로세스 / 시스템 / 계약 목록
   - 대응 필요 사항 및 기한

3. 대응 계획 수립
   - 담당자 지정
   - 정책/절차 개정 일정
   - 시스템 변경 필요 시 IT 협업
   - 직원 교육 계획

4. 이행 및 검증
   - 변경 사항 이행 완료 확인
   - 통제 테스트로 실효성 검증
   - 이행 완료 보고 (컴플라이언스 위원회)
```

---

## Board Reporting Template for Compliance Status

### 분기 이사회 컴플라이언스 보고서

```
[회사명] 컴플라이언스 현황 보고
보고 기간: [YYYY년 Q_]
보고자: [컴플라이언스 책임자 이름, 직책]

1. 핵심 요약 (Executive Summary)
   - 전반적 컴플라이언스 상태: [GREEN / YELLOW / RED]
   - 주요 성과: [2-3개 항목]
   - 주요 리스크: [2-3개 항목]
   - 이사회 결정 필요 사항: [있음 / 없음]

2. 규제 환경 변화
   - 신규 / 개정 법령: [목록]
   - 당사 영향: [영향 있음 / 없음 + 대응 현황]

3. 인시던트 현황
   - 이번 분기 발생 건수: [COUNT] (P1: _, P2: _, P3: _, P4: _)
   - 주요 인시던트 요약: [있을 경우]
   - 미해결 인시던트: [COUNT]

4. 핵심 KPI 현황
   [KPI 테이블 — 목표 vs. 실적]

5. 감사 결과
   - 내부 감사: [완료 / 진행 중] — 주요 발견 사항
   - 외부 감사: [완료 / 예정] — 주요 발견 사항

6. 다음 분기 계획
   - 주요 활동 및 일정

7. 예산 현황
   - 컴플라이언스 예산 집행률: [%]
   - 추가 예산 필요 여부: [있음 / 없음]
```
