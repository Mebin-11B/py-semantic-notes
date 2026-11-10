---
title: "Tenda firmware (multiple versions) contains hidden authentication backdoor"
url: https://kb.cert.org/vuls/id/213560
clipped: 2026-08-31 12:22:33
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Tenda firmware (multiple versions) contains hidden authentication backdoor](https://kb.cert.org/vuls/id/213560)

## Digest Summary
Several Tenda firmware versions (e.g., US_FH1201V1.0BR_V1.2.0.14, US_W15EV1.0br_V15.11.0.5, US_AC10V1.0re_V15.03.06.46, US_AC5V1.0RTL_V15.03.06.48, US_AC6V2.0RTL_V15.03.06.51) contain an undocumented authentication backdoor (CVE‑2026‑11405). In the web server binary (/bin/httpd), the login() function first attempts standard MD5 password verification; on failure it reads the configuration key “sys.rzadmin.password” and compares the supplied password directly via strcmp(). If the plaintext password matches, the function assigns admin role 2 and creates a valid session, while the username is not checked. This allows any attacker who knows the hidden password to obtain full administrative access to the device’s web interface, bypassing legitimate credentials. Exploitation enables reconfiguration, network setting changes, and disabling of security features. No vendor patch is available; mitigations include disabling remote web management and altering the default LAN IP to reduce exposure.

---

## Full Article

- [×](https://kb.cert.org/vuls/id/213560#)
      
- [Home](https://kb.cert.org/vuls/)
      
- [Notes](https://kb.cert.org/vuls/bypublished/desc/)
      
- [Search](https://kb.cert.org/vuls/search/)
      
- [Report a Vulnerability](https://kb.cert.org/vuls/report/)
      
- [Disclosure Guidance](https://kb.cert.org/vuls/guidance/)
      
- [VINCE](https://kb.cert.org/vince/)
    
    

  
  
  
    
      
      
        [Carnegie Mellon University](https://www.cmu.edu)
        
      
      
	
      
      
      
        
          
            
              
              
            
          
        
      
    
  
  
  

  
  
    
      
	

# [Software Engineering Institute](https://www.sei.cmu.edu/)
	

      
    
  
  
    
      

## CERT Coordination Center

    
  
  
  
    
      
        
          
- [Home](https://kb.cert.org/vuls/)
	  
- [Notes](https://kb.cert.org/vuls/bypublished/desc/) 
          
- [Search](https://kb.cert.org/vuls/search/)
          
- [Report a Vulnerability](https://kb.cert.org/vuls/report/)
          
- [Disclosure Guidance](https://kb.cert.org/vuls/guidance/)
	  
- [VINCE](https://kb.cert.org/vince/)
        
      
    
  
  
  
    
    

  

  
    
      
        

## Tenda firmware (multiple versions) contains hidden authentication backdoor	

      
    
    
      
        

#### Vulnerability Note VU#213560

        Original Release Date: 2026-07-06 | Last Revised: 2026-07-31
      
      
        
          
          
            
              
            
          
	  
          
          
            
              
            
          
          
          
          
            
              
            
          
          
        
       
    
    
      
    
  
  

  
    
      
        
	  
	  

### Overview

Several versions of Tenda firmware contain an undocumented authentication backdoor that grants administrative access to the devices' web management interfaces. An attacker can expoit this vulnerability, tracked as CVE-2026-11405, to bypass the password verification process and obtain full administrative control without valid credentials.

Affected Versions: 
* US_FH1201V1.0BR_V1.2.0.14(408)_EN_TD
* US_W15EV1.0br_V15.11.0.5(1068_1567_841)_EN_TDE
* US_AC10V1.0re_V15.03.06.46_multi_TDE01
* US_AC5V1.0RTL_V15.03.06.48_multi_TDE01
* US_AC6V2.0RTL_V15.03.06.51_multi_T

### Description

Tenda is a supplier of home and business network devices such as routers, switches, wireless access points, and video surveillance equipment. Most of these devices include web-based interfaces that allow users to perform configuration and management operations, which are protected by username/password authentication to prevent unauthorized modifications. 

The web server binary  `/bin/httpd`  contains an undocumented backdoor authentication mechanism in the  `login()`  function. Initially, the function follows a normal authentication path using MD5-based password verification. However, if authentication fails, the function invokes  `GetValue("sys.rzadmin.password")`  to retrieve an alternate password value from the device configuration. It then performs a direct  `strcmp()`  comparison in plaintext between the user-supplied password and the configuration-stored value. A successful match grants  `role=2`  admin-level access and creates a valid session. 

The associated username is not validated, so any provided username will succeed when paired with the backdoor password. This backdoor authentication mechanism is not documented or visible through any administrative interface.

### Impact

Successful exploitation grants full administrative access to the device's web interface, regardless of the configured administrator account credentials. With administrative control, an attacker can reconfigure the device, alter network settings, and disable security features, enabling broader compromise of the local network.

### Solution

Unfortunately, we were unable to reach the vendor to coordinate this vulnerability. Since a patch is unavailable, we can only offer mitigation strategies. The following workarounds can help mitigate this vulnerability's impact until a fixed version is released:

Disable remote management on your device
If your device supports remote web management, disable it. Disabling this feature prevents attackers on external networks from accessing your deviceâs administrative dashboard over the internet.

Restrict local network exposure
Changing the default LAN IP address may reduce opportunistic discovery by automated scanners that target known default IP ranges. Note that this measure does not prevent deliberate or targeted network scanning.

### Acknowledgements

Thanks to the reporter who wishes to remain anonymous. This document was written by Bob Kemerer.
	  
	
      
      
	
	  

### Vendor Information

	  
	  
  
    
    
      213560
      Filter by status:
      
        All
        Affected
        Not Affected
        Unknown
      
    
      
    
      Filter by content:
       Additional information available
    
    
       Sort by:
      
        Status
        Alphabetical
      
    
  

  
    [Expand all](https://kb.cert.org/vuls/id/213560#)
  
  
    
  

	  
	    

  
  
  
    
      
      

### 
	[Tenda](https://kb.cert.org/vuls/id/213560#Tenda)
	  
            
            
            
          
	
	
	  Affected 
	
      

      
	  
	  Notified:  2026-05-19
	  
	  Updated: 2026-07-31
	   
	   
      

Statement Date:   July 31, 2026
      
	
	  
	  
	  CVE-2026-11405 Affected
	  
	  
	  
	  
	
	
	

#### Vendor Statement

	
      

Tenda confirms multiple product firmware versions are affected by the hidden backdoor vulnerability tracked as CVE-2026-11405.
We have fully remediated this vulnerability: patched firmware versions for all affected models have been released to the public, and the corresponding official security advisory is published for users.
All vulnerability coordination tasks on Tendaâs side have been fully completed. We kindly request the CERT/CC team to close this case after review.
Official security advisory link: https://www.tendacn.com/notices/82662323598138
      
      
	
	

#### References

	
	
          
	  
	  
- [https://www.tendacn.com/notices/826623235981381](https://www.tendacn.com/notices/826623235981381)
	  
          
	
	
	
	
      
    
    
  
  
  

	  
	  
	
      
      
      
      
      
	
	  

### References

	  
	    
	    
	    
            
- [https://www.cisa.gov/audiences/high-risk-communities/projectupskill/module5](https://www.cisa.gov/audiences/high-risk-communities/projectupskill/module5)
            
          
	    
            
- [https://www.tendacn.com/download/](https://www.tendacn.com/download/)
            
          
	    
            
- [https://media.defense.gov/2023/Feb/22/2003165170/-1/-1/0/CSI_BEST_PRACTICES_FOR_SECURING_YOUR_HOME_NETWORK.PDF](https://media.defense.gov/2023/Feb/22/2003165170/-1/-1/0/CSI_BEST_PRACTICES_FOR_SECURING_YOUR_HOME_NETWORK.PDF)
            
          
	  
	  
	
      
      
      

### Other Information

        
          
            
	      
              
                CVE IDs:
		
		
		
                [CVE-2026-11405](https://www.cve.org/CVERecord?id=CVE-2026-11405)
		
                
		
	      
	      
              
                API URL: 
                [VINCE JSON](https://kb.cert.org/vuls/api/213560/) | [CSAF](https://kb.cert.org/vuls/api/213560/csaf/)
              
	      
		
		  Date Public:
		
                2026-07-06
              
              
                Date First Published:
                2026-07-06
              
              
                Date Last Updated: 
                2026-07-31 19:19 UTC
              
              
                Document Revision: 
                2 
              
            
          
	
    
  
  
  
    
      
	
- [About vulnerability notes](https://certcc.github.io/CERT-Guide-to-CVD/reference/policy_templates/receivers/?h=vulnerability+notes)
	
- [Contact us about this vulnerability](mailto:cert@cert.org?Subject=VU%23213560 Feedback)
	
- [Provide a vendor statement](https://certcc.github.io/VINCE-docs/Case-Handling/)
      
    
  

    

    
  
  
  
  

  
    
      

Sponsored by [CISA.](https://www.cisa.gov/cybersecurity) 
    
  

  
    
      
	
	[Download PGP Key](https://certcc.github.io/pgp)
      
    
    
      
        

[Read CERT/CC Blog](https://insights.sei.cmu.edu/cert/)
        
      
    
    
      
	

[Learn about Vulnerability Analysis](https://www.sei.cmu.edu/research-capabilities/all-work/display.cfm?customel_datapageid_4050=21304)
      
    
  

  
    
      
	
	  

	    Carnegie Mellon University
	    
	    Software Engineering Institute
	    
	    4500 Fifth Avenue
	    
	    Pittsburgh, PA 15213-2612
	    
	    [412-268-5800](tel:+14122685800)
	    
	  
	
	
	  
	    
- 
	    
- 
	    
- 
	    
- 
	    
- 
	  
	
      
      
	
	  
	    [Office Locations](http://www.sei.cmu.edu/locations/index.cfm) | [Additional Sites Directory](http://www.sei.cmu.edu/additional-sites-directory/index.cfm) | [Legal](https://certcc.github.io/VINCE-docs/VINCE-Code-of-Conduct/) | [Privacy Notice](https://www.sei.cmu.edu/legal/privacy-notice/index.cfm) |  [CMU Ethics Hotline](https://www.cmu.edu/hr/ethics-hotline/) | [www.sei.cmu.edu](http://www.sei.cmu.edu)
	  
	
      
      
	
          Â©2026 Carnegie Mellon University
	
      
    
    
      [Contact SEI](https://www.sei.cmu.edu/contact-us/)

      
	    

#### Contact CERT/CC

            

[412-268-5800](tel:+14122685800)
	    
             [cert@cert.org](mailto:cert@cert.org)
