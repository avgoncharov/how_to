using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Text;

namespace SimpleTcpServer
{
	public class RequestProcessor
	{
		public void Proccess(TcpClient client)
		{	
			var buf = new byte[client.ReceiveBufferSize];
			client.GetStream().Read(buf, 0, buf.Length);

			var content = String.Format("<html><body><h2>Hello</h2><h2>Word</h2><div>at {0} UTC.</div></body></html>\r\n\r\n", DateTime.UtcNow);
			var buf2 = Encoding.UTF8.GetBytes(content);
			var answer = Encoding.UTF8.GetBytes(String.Format("HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: {0}\r\n\r\n{1}", buf2.Length, content));

 			client.GetStream().Write(answer, 0, answer.Length);
		}
	}
}
