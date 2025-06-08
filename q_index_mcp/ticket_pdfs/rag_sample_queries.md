# RAG Sample Queries for Voice Receptionist JIRA Tickets

## Technical Troubleshooting Queries

### Network & Connectivity Issues
1. **"What are the common causes of WebSocket connection failures in the Voice Receptionist system?"**
   - *Expected retrieval: ABC-2847 (WebSocket failures), ABC-2854 (TLS certificate issues)*
   - *Context: Network connectivity problems, SSL/TLS handshake errors*

2. **"How do we resolve high latency and packet loss issues affecting voice quality?"**
   - *Expected retrieval: ABC-2851 (voice quality degradation)*
   - *Context: Multi-site deployment, network optimization solutions*

3. **"What SSL/TLS certificate issues can cause connection drops in enterprise environments?"**
   - *Expected retrieval: ABC-2854 (TLS certificate validation failures)*
   - *Context: Corporate firewalls, certificate chain validation*

### Audio & Voice Quality
4. **"What solutions exist for DTMF tone detection problems with mobile callers?"**
   - *Expected retrieval: ABC-2818 (DTMF detection accuracy issues)*
   - *Context: Mobile carrier compatibility, background noise suppression*

5. **"How can we fix one-way audio issues specific to Firefox browsers?"**
   - *Expected retrieval: ABC-2841 (Firefox codec negotiation failures)*
   - *Context: Browser compatibility, WebRTC implementation differences*

6. **"What causes robotic or distorted audio in voice communications?"**
   - *Expected retrieval: ABC-2851 (voice quality degradation)*
   - *Context: Packet loss, jitter, codec optimization*

### Performance & Scalability
7. **"How do we handle database connection pool exhaustion during peak loads?"**
   - *Expected retrieval: ABC-2832 (database connection pool exhaustion)*
   - *Context: Connection pooling, database scaling, performance optimization*

8. **"What are effective solutions for memory leaks in long-running browser sessions?"**
   - *Expected retrieval: ABC-2825 (WebRTC memory leaks)*
   - *Context: Browser crashes, memory management, garbage collection*

9. **"How should we configure rate limiting to handle legitimate traffic spikes?"**
   - *Expected retrieval: ABC-2839 (HTTP 429 rate limiting)*
   - *Context: Campaign traffic, burst handling, dynamic rate limiting*

## Business Impact & Resolution Queries

### Customer Experience
10. **"What business impacts occur when voice quality degrades in customer-facing systems?"**
    - *Expected retrieval: ABC-2851, ABC-2818, ABC-2841*
    - *Context: Customer satisfaction, revenue impact, operational costs*

11. **"How much downtime and revenue loss can WebSocket failures cause?"**
    - *Expected retrieval: ABC-2847 (WebSocket failures)*
    - *Context: Service outages, business continuity, SLA impacts*

### Resolution Strategies
12. **"What verification steps should be performed after fixing voice quality issues?"**
    - *Expected retrieval: ABC-2818, ABC-2825, ABC-2851*
    - *Context: Testing methodologies, customer validation, monitoring*

13. **"How do we implement proper cleanup for WebRTC connections to prevent memory issues?"**
    - *Expected retrieval: ABC-2825 (memory leaks)*
    - *Context: Resource management, garbage collection, connection lifecycle*

## Cross-Functional Queries

### Browser Compatibility
14. **"What browser-specific issues affect Voice Receptionist functionality?"**
    - *Expected retrieval: ABC-2841 (Firefox issues), ABC-2825 (Chrome memory leaks)*
    - *Context: Cross-browser compatibility, WebRTC implementations*

15. **"How do different browsers handle WebRTC peer connections and what problems arise?"**
    - *Expected retrieval: ABC-2841, ABC-2825*
    - *Context: Browser differences, codec negotiation, memory management*

### Enterprise Deployment
16. **"What security and network challenges exist in enterprise Voice Receptionist deployments?"**
    - *Expected retrieval: ABC-2854 (TLS issues), ABC-2851 (multi-site deployment)*
    - *Context: Corporate security, SSL inspection, network architecture*

17. **"How do corporate firewalls and security appliances interfere with voice communications?"**
    - *Expected retrieval: ABC-2854 (TLS certificate validation)*
    - *Context: SSL inspection, DPI, certificate handling*

### Load Management
18. **"What strategies prevent service disruption during high-traffic events like marketing campaigns?"**
    - *Expected retrieval: ABC-2839 (rate limiting), ABC-2832 (database scaling)*
    - *Context: Traffic spikes, capacity planning, burst handling*

19. **"How do we scale Voice Receptionist systems for peak concurrent usage?"**
    - *Expected retrieval: ABC-2832, ABC-2847, ABC-2839*
    - *Context: Database scaling, connection management, load balancing*

## Diagnostic & Monitoring Queries

### Error Analysis
20. **"What error logs indicate WebSocket connection problems?"**
    - *Expected retrieval: ABC-2847 (WebSocket failures)*
    - *Context: Log analysis, error patterns, debugging techniques*

21. **"How do we identify and diagnose memory leak patterns in browser applications?"**
    - *Expected retrieval: ABC-2825 (memory leaks)*
    - *Context: Memory profiling, garbage collection monitoring*

### Preventive Measures
22. **"What monitoring and alerting should be implemented to prevent voice system outages?"**
    - *Expected retrieval: ABC-2832, ABC-2847*
    - *Context: Proactive monitoring, alert thresholds, health checks*

23. **"How can we proactively detect and prevent certificate-related connection issues?"**
    - *Expected retrieval: ABC-2854 (TLS certificate issues)*
    - *Context: Certificate monitoring, validation checks, renewal processes*

## Industry-Specific Queries

### Healthcare
24. **"What special considerations exist for Voice Receptionist systems in healthcare environments?"**
    - *Expected retrieval: ABC-2841 (HealthCare Systems LLC)*
    - *Context: HIPAA compliance, patient intake, Firefox compatibility*

### Call Centers
25. **"How do we prevent browser crashes for agents using Voice Receptionist for extended periods?"**
    - *Expected retrieval: ABC-2825 (CallCenter Pro memory issues)*
    - *Context: Agent productivity, browser stability, memory management*

### Enterprise Sales
26. **"What voice system issues can impact sales demonstrations and client presentations?"**
    - *Expected retrieval: ABC-2854 (SecureTech Enterprises)*
    - *Context: Enterprise security, SSL inspection, presentation reliability*