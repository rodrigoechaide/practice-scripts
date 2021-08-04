import dns.resolver

for i in range(10):
  result = dns.resolver.resolve('rodrigoechaide.com.ar', 'A')
  for ipval in result:
    print('IP', ipval.to_text())