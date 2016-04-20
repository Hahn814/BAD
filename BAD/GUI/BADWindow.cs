using InTheHand.Net;
using InTheHand.Net.Bluetooth;
using InTheHand.Net.Sockets;
using System;
using System.Drawing;
using System.IO;
using System.Net;
using System.Windows.Forms;

namespace CollectTarget
{
    public partial class BADWindow : Form
    {
        private string currentDirectory = "";
        private string file, fullPath;
        private string ftpURL = "ftp://ndrives.calu.edu";
        private string username = "";
        private string password = "";
        private string cameraType = "gopro";

        private bool noneSelected = false;
        public BADWindow()
        {
            InitializeComponent();
            
        }


        private void updateDirectory_Click(object sender, EventArgs e)
        {
            //method to update the current directory and re-populate the image directory list
        }

        private void buildFile(string filename, string ftpURL, string ftpPsk, string camera)
        {
            string[] lines = new string[2];
            lines[0] = filename;
            lines[1] = camera;

            System.IO.File.WriteAllLines(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName+"/autogendata.txt", lines);  
        }
        private void continueButton_Click(object sender, EventArgs e)
        {
            //method to test for validity and upload target to edison 
            errorMessage.ForeColor = Color.Black;
            errorMessage.Text = "Initializing communications with Edison..";
            ftpURL = ftpAddressTb.Text;
            password = ftpPskTb.Text;
            username = ftpUserTb.Text;
            errorMessage.AppendText("User: " + username + "\n" + ftpURL + "\n");
          

                try
            {
                // Get the object used to communicate with the server.
                FileInfo fi = new FileInfo(fullPath);
                buildFile(fi.Name, ftpURL, password, cameraType);
                FtpWebRequest request = (FtpWebRequest)WebRequest.Create(ftpURL + "/" + fi.Name);
                
                request.Method = WebRequestMethods.Ftp.UploadFile;
                errorMessage.AppendText("Connecting with.. " + ftpURL + "\n");

                // This example assumes the FTP site uses anonymous logon.
                request.Credentials = new NetworkCredential(username, password);

                // Copy the contents of the file to the request stream
                byte[] fileContents;

                errorMessage.AppendText("Writing " + fullPath + " to " + ftpURL + "\n");
                fileContents = File.ReadAllBytes(fullPath);
                request.ContentLength = fileContents.Length;
                // write image to server
                Stream requestStream = request.GetRequestStream();
                requestStream.Write(fileContents, 0, fileContents.Length);

                requestStream.Close();

                // Get the object used to communicate with the server.
                fullPath = Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName + "/autogendata.txt";
                fi = new FileInfo(fullPath);
                request = (FtpWebRequest)WebRequest.Create(ftpURL + "/" + fi.Name);

                request.Method = WebRequestMethods.Ftp.UploadFile;
                errorMessage.AppendText("Preparing tranfer of autgen data " + ftpURL + "\n");

                // This example assumes the FTP site uses anonymous logon.
                request.Credentials = new NetworkCredential(username, password);

                errorMessage.AppendText("Writing autogen data to: " + ftpURL + "\n");
                fileContents = File.ReadAllBytes(fullPath);
                request.ContentLength = fileContents.Length;
                // write image to server
                requestStream = request.GetRequestStream();
                requestStream.Write(fileContents, 0, fileContents.Length);

                requestStream.Close();

                FtpWebResponse response = (FtpWebResponse)request.GetResponse();
                errorMessage.AppendText(ftpURL + "::" + response.StatusDescription + "\n");


                response.Close();
                continueButton.Enabled = false;
            }
            catch(Exception f)
            {
                errorMessage.AppendText(f.ToString());
            }
        }

        private void BADWindow_Load(object sender, EventArgs e)
        {
            currentDirectory    = System.IO.Directory.GetCurrentDirectory();
            imageName.Text      = "Target Image File Descriptor";
            
        }

        private void browse_Click(object sender, EventArgs e)
        {
			//Open a file browser window for the user to choose an image
            OpenFileDialog ofd = new OpenFileDialog();
            errorMessage.Text = "";

            //File browser restraints ~ only image files are okay
            ofd.Filter = "Image Files(*.BMP; *.JPG; *.PNG; *.GIF)| *.BMP; *.JPG; *.GIF; *.PNG; | All files(*.*) | *.*";
            ofd.Title = "Select an Image File";

            if (ofd.ShowDialog() == DialogResult.OK)
            {
                // assign the image file chosen to the file variable, seperate full path and image name.
                file = ofd.FileName;
                fullPath = file;
                file = file.Substring(file.LastIndexOf("\\")).Remove(0,1);
                imageName.Text = file;
                button1.Enabled = true;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if(!imageList.Items.Contains(file))
            {
                imageList.Items.Add(file, true);
                button1.Enabled = false;
                continueButton.Enabled = true;
            }
            else
            {
                errorMessage.Text = "Duplicate entry detected";
            }
        }

        private void testFtpButton_Click(object sender, EventArgs e)
        {
            //method to test for validity and upload target to edison 
            errorMessage.ForeColor = Color.Black;
            ftpURL = ftpAddressTb.Text;
            password = ftpPskTb.Text;
            username = ftpUserTb.Text;

            try
            {
                // Get the object used to communicate with the server.
                FtpWebRequest request = (FtpWebRequest)WebRequest.Create(ftpURL + "/" + "test.txt");
                request.Method = WebRequestMethods.Ftp.UploadFile;
                errorMessage.AppendText("Connecting with " + ftpURL + " as (" + username + ")\n");

                // This example assumes the FTP site uses anonymous logon.
                request.Credentials = new NetworkCredential(username, password);

                FtpWebResponse response = (FtpWebResponse)request.GetResponse();
                errorMessage.AppendText("Successful Connection " + response.StatusDescription + "\n");

                response.Close();
                
            }
            catch (Exception f)
            {
                errorMessage.AppendText(f.ToString());
            }
        }
        private void enabledTestButton()
        {
            if (ftpAddressTb.TextLength > 0 && ftpPskTb.TextLength > 0 && ftpUserTb.TextLength > 0)
            {
                testFtpButton.Enabled = true;
            }
            else
            {
                testFtpButton.Enabled = false;
            }
        }
        private void ftpAddressTb_TextChanged(object sender, EventArgs e)
        {
            enabledTestButton();
        }

        private void ftpPskTb_TextChanged(object sender, EventArgs e)
        {
            enabledTestButton();
        }

        private void goProRb_CheckedChanged(object sender, EventArgs e)
        {
            if(goProRb.Checked)
            {
                cameraType = "gopro";
            }
            
        }

        private void usbCameraRb_CheckedChanged(object sender, EventArgs e)
        {
            if(usbCameraRb.Checked)
            {
                cameraType = "usb";
            }
            
        }

        private void imageList_SelectedIndexChanged(object sender, EventArgs e)
        {

            if(imageList.CheckedItems.Count == 0)
            {
                continueButton.Enabled = false;
                errorMessage.Text = "One image file must be selected";
                noneSelected = true;
            }
            else if (noneSelected.Equals(true))
            {
                errorMessage.Clear();
                noneSelected = false;
            }

            imagePreview.ImageLocation = fullPath;
            imagePreview.SizeMode = PictureBoxSizeMode.StretchImage;

        }
    }


}
