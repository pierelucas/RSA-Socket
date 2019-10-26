### RSA - Socket

    RSA Encrypted UDP Socket module
    
    Usage:
    
    Server:
    from server import Receiver
    sock = Receiver(ip, port, buffer_size)
    sock.start_receive()
    
    Client:
    from client import Sender
    sock = Sender(ip, port, data)
    sock.send_udp()
    
+ Author: PiereLucas(Julian Huch)