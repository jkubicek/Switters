class Switters < Formula
  homepage "https://github.com/jkubicek/switters"
  url "https://github.com/jkubicek/Switters/archive/0.1.2.tar.gz"
  sha1 "de75246b72f46e151beef42adb7eb9d6137086f7"
  version "0.1.3"
  depends_on :python if MacOS.version <= :snow_leopard
  
  resource "tweetpony" do
    url "https://pypi.python.org/packages/source/T/TweetPony/tweetpony-1.4.2.tar.gz"
    sha1 "f00ee5c9f5c8e01abb5af026125690a0eee1b705"
  end
  
  resource "qrcode" do
    url "https://pypi.python.org/packages/source/q/qrcode/qrcode-5.1.tar.gz"
    sha1 "686d017fb655fa2f1d600b1a8672f5ee538ec2d6"
  end
  
  resource "requests" do
    url "https://pypi.python.org/packages/source/r/requests/requests-2.5.1.tar.gz"
    sha1 "f906c441be2f0e7a834cbf701a72788d3ac3d144"
  end

  def install
    ENV.prepend_create_path "PYTHONPATH", libexec/"vendor/lib/python2.7/site-packages"
    %w[tweetpony qrcode requests].each do |r|
      resource(r).stage do
        system "python", *Language::Python.setup_install_args(libexec/"vendor")
      end
    end

    ENV.prepend_create_path "PYTHONPATH", libexec

    libexec.install Dir["switterslib"]
    libexec.install Dir["zxing"]
    libexec.install Dir["zxing_java"]
    bin.install "switters"

    bin.env_script_all_files(libexec/"bin", :PYTHONPATH => ENV["PYTHONPATH"])
  end

  test do
    system "#{bin}/switters", "-h"
  end
end
