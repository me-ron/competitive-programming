class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_visited={}
        for i in range (len(cpdomains)):
            num,domain=cpdomains[i].split()
            num=int(num)
            domain=domain.split(".")
            for j in range(len(domain)):
                if ".".join(domain[j:]) in domain_visited:
                    domain_visited[".".join(domain[j:])]+=num
                else:
                    domain_visited[".".join(domain[j:])]=num
        return[f"{domain_visited[i]} {i}" for i in domain_visited]
        
            

        
        
        