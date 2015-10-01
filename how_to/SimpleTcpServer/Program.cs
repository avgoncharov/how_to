using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

namespace SimpleTcpServer
{
	class Program
	{
		static void Main(string[] args)
		{
			var server = new TcpServer("127.0.0.1", 1221);
			server.Start();
			
			Console.WriteLine("Server started.");
			Console.Write("To quit, press eny key.");
			Console.ReadKey();
			
			server.Stop();
						
			Console.WriteLine();
			Console.WriteLine("Complete.");
		}
	}
}
