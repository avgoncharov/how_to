/*
The MIT License (MIT)

Copyright (c) 2014 Goncharov Andrey.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
 */
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Mail;
using System.Text;

namespace send_mail
{
	/// <summary>
	/// This program demonstrates how to send mail in .NET by using smtp-client.
	/// </summary>
	class Program
	{
		static int Main(string[] args)
		{
			string mailFrom = "userFrom@fromDomainName.com";
			string mailTo = "userTo@toDomainName.ru";

			if (args.Length >= 2) {// First argument - mailFrom, second - mailTo.
				mailFrom = args[0];				
				mailTo = args[1];
			}

			Console.WriteLine(mailFrom);
			Console.WriteLine(mailTo);

			using (var msg = new MailMessage(mailFrom, mailTo)) {
				msg.Subject = "Test mail";
				msg.Body = "<h4>This is test mail.</h4><div style=\"color:gray\">Hello.</div>";
				msg.IsBodyHtml = true;

				// If we pass three arguments and last argument is equal to '-def'  then program uses hardcoding, otherwise program uses app.config.
				using (var smtp = CreateSmtp(args.Length == 3 ? args[2] == "-def": false)) {
					try {
						smtp.Send(msg);
						Console.WriteLine("Ok");
						return 0;
					}
					catch (Exception ex) {
						Console.WriteLine(ex.ToString());
						return 1;
					}
				}
			}
		}

		#region Private
		private static SmtpClient CreateSmtp(bool useDefault = false)
		{
			Console.WriteLine(useDefault);
			if (!useDefault)
				return new SmtpClient();


			var smtp = new SmtpClient("smtp.gmail.com", 587) {
				DeliveryMethod = SmtpDeliveryMethod.Network,
				UseDefaultCredentials = false,
				EnableSsl = true,
				Credentials = new NetworkCredential("userName", "password")
			};

			return smtp;
		}
		#endregion
	}
}
