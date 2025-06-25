#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const minimist = require('minimist');
const { OpenAI } = require('openai');

const argv = minimist(process.argv.slice(2), {
  string: ['model'],
  alias: { m: 'model', h: 'help', v: 'version' }
});

if (argv.help) {
  console.log(`Usage: codex [options] <prompt>

Options:
  -m, --model <model>  Model to use (default: gpt-3.5-turbo)
  -h, --help           Show this help message
  -v, --version        Show package version`);
  process.exit(0);
}
if (argv.version) {
  const pkg = require('../package.json');
  console.log(pkg.version);
  process.exit(0);
}

const prompt = argv._.join(' ').trim();
if (!prompt) {
  console.error('No prompt provided.');
  process.exit(1);
}

const apiKey = process.env.OPENAI_API_KEY;
if (!apiKey) {
  console.error('OPENAI_API_KEY environment variable not set.');
  process.exit(1);
}

const model = argv.model || 'gpt-3.5-turbo';

async function run() {
  const openai = new OpenAI({ apiKey });
  try {
    const completion = await openai.chat.completions.create({
      messages: [{ role: 'user', content: prompt }],
      model
    });
    const content = completion.choices[0]?.message?.content || '';
    console.log(content.trim());
  } catch (err) {
    console.error('Error:', err.message || err);
    process.exit(1);
  }
}

run();
