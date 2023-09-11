const { spawn } = require('child_process');

module.exports = async (req, res) => {
  const process = spawn('python', ['app.py']);

  process.stdout.on('data', (data) => {
    res.status(200).send(data.toString());
  });

  process.stderr.on('data', (data) => {
    console.error(`Error: ${data}`);
  });

  process.on('close', (code) => {
    if (code === 0) {
      console.log('Process finished successfully');
    } else {
      console.error(`Process exited with code ${code}`);
      res.status(500).send('Internal Server Error');
    }
  });
};
