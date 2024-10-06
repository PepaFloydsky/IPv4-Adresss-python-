class ipv4:
        def __init__(self,adress):
                self.adress = adress 
                self.octets = self.adress.split(".")
        def Octet(self):
            
            return len(self.octets)
        def Private(self):
            
            if self.octets[0] == "10" or self.octets[0] == "192" or self.octets[0] == "172":
                   return "IsPrivate: True"
            else:
                   return "Isprivate: False "
            
        def Isvalid(self):
            if len(self.octets) != 4:
                   return"IsValid: False"
                   
            else: 
                    return"IsValid: True "
        def Getclass(self):
                First_Octet = int(self.octets[0])
                if 0 <= First_Octet < 128:
                       return "Class: A"
                elif 192 <= First_Octet < 224:
                     return "Class: C"
                elif 128 <= First_Octet < 192:
                    return "Class: B"
                elif 224 <= First_Octet < 240:
                    return "Class: D"
                elif 240 <= First_Octet <= 255:
                    return "Class: E"
                else: 
                      return "Class: Invalid"
        
        def To_bin(self):
              Second_Octet = format(int(self.octets[1]),'08b')
              Third_Octet = format(int(self.octets[2]),'08b')
              Fourth_Octet = format(int(self.octets[3]),'08b')
              First_Octet = format(int(self.octets[0]),'08b')
              return First_Octet,Second_Octet,Third_Octet,Fourth_Octet


            

            
            
  
ip =ipv4("180.168.1.1")
print("Octet",ip.Octet())
print(ip.Private())
print(ip.Isvalid())
print(ip.Getclass())
print(ip.To_bin())

