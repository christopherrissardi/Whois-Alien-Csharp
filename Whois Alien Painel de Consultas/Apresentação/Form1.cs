﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Whois_Alien_Painel_de_Consultas.Apresentação;

namespace Whois_Alien_Painel_de_Consultas
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void btn_login_Click(object sender, EventArgs e)
        {
            try
            {
                if (txtUsuario.Text.Equals("abc") && txtSenha.Text.Equals("123"))
                {
                    //SLA
                }
                else
                {
                    MessageBox.Show("Error", "Username or password invalid", MessageBoxButtons.OK, MessageBoxIcon.Error);

                }catch (Exception ex)
            {
                MessageBox.Show("Error", "Username or password invalid", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            {

            }
            }
        }

        private void btn_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
