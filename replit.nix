{ pkgs }: {
  deps = [
    pkgs.nodePackages.prettier
    pkgs.glibcLocales
    pkgs.bashInteractive
    pkgs.nodePackages.bash-language-server
    pkgs.man
  ];
}